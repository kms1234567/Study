#include <stdio.h>
#include "csapp.h"

/* Recommended max cache and object sizes */
#define MAX_CACHE_SIZE 1049000
#define MAX_OBJECT_SIZE 102400
#define LRU_MAGIC_NUMBER 9999
// Least Recently Used
// LRU: 가장 오랫동안 참조되지 않은 페이지를 교체하는 기법

#define CACHE_OBJS_COUNT 10

/* You won't lose style points for including this long line in your code */
static const char *user_agent_hdr =
    "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:10.0.3) Gecko/20120305 "
    "Firefox/10.0.3\r\n";
static const char *requestline_hdr_format = "GET %s HTTP/1.0\r\n";
static const char *endof_hdr = "\r\n";
static const char *host_hdr_format = "Host: %s\r\n";
static const char *conn_hdr = "Connection: close\r\n";
static const char *prox_hdr = "Proxy-Connection: close\r\n";

static const char *host_key = "Host";
static const char *connection_key = "Connection";
static const char *proxy_connection_key = "Proxy-Connection";
static const char *user_agent_key = "User-Agent";

void *thread(void *vargsp);
void doit(int connfd);
void parse_uri(char *uri, char *hostname, char *path, int *port);
void build_http_header(char *http_header, char *hostname, char *path, int port, rio_t *client_rio);
int connect_endServer(char *hostname, int port);

// cache function
void cache_init();
int cache_find(char *url);
void cache_uri(char *uri, char *buf);

void readerPre(int i);
void readerAfter(int i);

typedef struct 
{
  char cache_obj[MAX_OBJECT_SIZE];
  char cache_url[MAXLINE];
  int LRU;
  int isEmpty;

  int readCnt;        // count of readers
  sem_t wmutex;       // 캐시데이터에 접근하는 것을 보호하는 용도
  sem_t rdcntmutex;   // readcnt 데이터에 접근하는 것을 보호하는 용도
}cache_block;

typedef struct
{
  cache_block cacheobjs[CACHE_OBJS_COUNT];  // ten cache blocks
  int cache_num;
}Cache;

/* 캐시는 전역 변수 (공유자원) */
Cache cache;

/* 클라이언트와 서버 사이에 프록시 서버를 두고, 쓰레드를 이용한 동시성 서버를 구축하며, 세마포어를 이용해 LRU 캐싱을 구현한 코드 */
int main(int argc, char **argv) {
  int listenfd, *connfdp;
  socklen_t clientlen;
  char hostname[MAXLINE], port[MAXLINE];
  pthread_t tid;
  struct sockaddr_storage clientaddr;

  /* 캐시 초기화 */
  cache_init();

  if (argc != 2) {
    fprintf(stderr, "usage: %s <port> \n", argv[0]);
    exit(1);  
  }
  /* 
   * 소켓 연결이 종료되었는데 send()를 하면 -1을 리턴하며 errno를 EPIPE로 설정된다.(상대편은 연결 종료 완료) 
   * 즉, 읽기가 안되는 파이프에 쓰려고 한다면, SIGPIPE 시그널이 발생하는데, SIGPIPE의 기본 핸들러는 프로세스 종료이므로, 갑자기 프로세스가 종료될 수 있다. 
   * Singal()의 SIG_IGN을 통해 해당 시그널을 무시하는 절차가 있어야 한다.
   */
  Signal(SIGPIPE, SIG_IGN); 

  /* 입력받은 포트를 통해 듣기 식별자를 생성 */
  listenfd = Open_listenfd(argv[1]);
  while (1) {
    clientlen = sizeof(clientaddr);
    /* 클라이언트와 연결 후, 연결 식별자를 리턴받음 */

    /* 
     * 여기서 connfdp를 동적할당해서 받는 이유는 뭘까 ._.? 
     * 만약 동적할당 없이 전달되고, 피어 쓰레드가 인자를 받고 myid 할당 전에 메인쓰레드로 preempt 당한다고 가정하자.  
     * 메인쓰레드에서 다음 Accept를 수행하게 되면, 전에 있던 connfd가 변경된다. - (메인쓰레드의 주소값을 전달했기때문에 값이 변경됨)
     * 그래서 동적할당 후, Accept의 결과를 *connfdp로 받게 되면, preempt 당하더라도 다음 Accept는 동적할당으로 다음 가용블록에 데이터를 넣기 때문에
     * 기존 피어쓰레드의 *connfdp(주소값)가 수정될 일은 없다! 
     * 혹은 (void*)connfd 로전달하여 임시 주소에 값을 저장 후, 주소값을 전달한다. void*는 저장할 때 끝주소는 모르지만 시작 주소를 알고있다.
     * 요약 : 같은 주소공간이 아니라 다른 주소공간을 참조하게 하자. 
     */
    connfdp = Malloc(sizeof(int));
    *connfdp = Accept(listenfd, (SA *)&clientaddr, &clientlen);

    Getnameinfo((SA *)&clientaddr, clientlen, hostname, MAXLINE, port, MAXLINE, 0);
    printf("Accepted connection from (%s %s).\n", hostname, port);

    /* 피어쓰레드를 생성하며, 인자(듣기식별자)와 함께 thread 함수로 분기한다. */
    Pthread_create(&tid, NULL, thread, connfdp);
  }
  return 0;
}

void *thread(void *vargsp) {
  int connfd = *((int*)vargsp);
  /* 
   * 해당 쓰레드는 다른 쓰레드와 분리함으로써 쓰레드가 종료되면 자원을 반납하게 된다. 
   * 만약, 분리하지 않으면 메인쓰레드가 끝나기 전 혹은 다른 쓰레드에 의해 청소되기 전까지는 사용되지 않는 쓰레드(기)들이 넘쳐나게 된다.
   */
  Pthread_detach(pthread_self());
  /* 동적할당한 인자는 Free를 해줘야함 */
  Free(vargsp);
  doit(connfd);
  Close(connfd);
}

void doit(int connfd) {
  /* 끝단 서버 디스크립터 */
  int end_serverfd;

  char buf[MAXLINE], method[MAXLINE], uri[MAXLINE], version[MAXLINE];
  char endserver_http_header[MAXLINE];
  char hostname[MAXLINE], path[MAXLINE];
  int port;
  
  /* rio: 클라이언트와의 통신을 위한 / server_rio: 끝단서버와의 통신을 위한 */
  rio_t rio, server_rio;

  Rio_readinitb(&rio, connfd);
  Rio_readlineb(&rio, buf, MAXLINE);
  sscanf(buf, "%s %s %s", method, uri, version);  // 클라이언트 요청 라인을 method uri version에 저장한다.

  if (strcasecmp(method, "GET")) {
    printf("Proxy does not implement the method");
    return;
  } 
  
  char url_store[100];
  strcpy(url_store, uri);

  /* 캐시인덱스 변수 */
  int cache_index;

  /* 만약 캐시되어있다면 캐시인덱스의 데이터를 클라이언트에게 바로 전달해준다. */
  if ((cache_index=cache_find(url_store)) != -1) {
    readerPre(cache_index);
    Rio_writen(connfd, cache.cacheobjs[cache_index].cache_obj, strlen(cache.cacheobjs[cache_index].cache_obj));
    readerAfter(cache_index);
    return;
  }  
  
  //////////////////////// 캐시가 되어있지 않아서 끝단 서버까지 가야하는 상황 ////////////////////////

  // uri로 hostname, path port를 추출(파싱)한다.
  parse_uri(uri, hostname, path, &port);

  // 서버로보낼 헤더를 생성한다. (endserver_http_header에 저장)
  build_http_header(endserver_http_header, hostname, path, port, &rio);

  // 끝단 서버와 연결한다. (헤더를 굳이 가져가는 이유는>)
  end_serverfd = connect_endServer(hostname, port);
  if (end_serverfd < 0) {
    printf("connection failed\n");
    return;
  }

  Rio_readinitb(&server_rio, end_serverfd);
  // 끝단 서버에 헤더를 전송한다.
  Rio_writen(end_serverfd, endserver_http_header, strlen(endserver_http_header));

  // 받은 메시지를 클라이언트에게 전송한다.
  char cachebuf[MAX_OBJECT_SIZE];
  int sizebuf = 0;
  size_t n;
  while ((n=Rio_readlineb(&server_rio, buf, MAXLINE)) != 0) {
    sizebuf += n;
    if (sizebuf < MAX_OBJECT_SIZE)
      strcat(cachebuf, buf);
    Rio_writen(connfd, buf, n);
  }
  Close(end_serverfd);

  // 캐시에 저장한다.
  if (sizebuf < MAX_OBJECT_SIZE) {
    cache_uri(url_store, cachebuf);
  }
}

/* 엔드서버에게 보낼 헤더를 http_header에 작성한다. */
void build_http_header(char *http_header, char *hostname, char *path, int port, rio_t *client_rio) {
  char buf[MAXLINE], request_hdr[MAXLINE], other_hdr[MAXLINE], host_hdr[MAXLINE];
  
  // request line
  sprintf(request_hdr, requestline_hdr_format, path);

  // get other request header for client rio and change it
  while (Rio_readlineb(client_rio, buf, MAXLINE) > 0) {
    if (strcmp(buf, endof_hdr) == 0)
      break;  // EOF
    
    if (!strncasecmp(buf, host_key, strlen(host_key))) {
      strcpy(host_hdr, buf);
      continue;
    }

    if (!strncasecmp(buf, connection_key, strlen(connection_key))
      && !strncasecmp(buf, proxy_connection_key, strlen(proxy_connection_key))
      && !strncasecmp(buf, user_agent_key, strlen(user_agent_key))) {
        strcat(other_hdr, buf);
      }
  }

  if (strlen(host_hdr) == 0) {
    sprintf(host_hdr, host_hdr_format, hostname);
  }
  sprintf(http_header, "%s%s%s%s%s%s%s",
          request_hdr,
          host_hdr,
          conn_hdr,
          prox_hdr,
          user_agent_hdr,
          other_hdr,
          endof_hdr);
  return;
}

// Connect to the end server
inline int connect_endServer(char *hostname, int port) {
  char portStr[100];
  sprintf(portStr, "%d", port);
  return Open_clientfd(hostname, portStr);
}

// hostname, path, port를 uri에서 파싱한다.
void parse_uri(char *uri, char *hostname, char *path, int *port) {
  *port = 80;
  char *pos = strstr(uri, "//");

  /* pos가 '//' 바로 뒤를 가리키도록 한다. */
  pos = pos!=NULL? pos+2:uri;

  /* pos2가 ':' 바로 뒤를 가리키도록 한다. */
  char *pos2 = strstr(pos, ":");

  if (pos2 != NULL) {
    // hostname, port, path 를 저장한다.
    *pos2 = '\0';
    sscanf(pos, "%s", hostname);
    sscanf(pos2+1, "%d%s", port, path);
  } else {
    // 만약 포트가 적혀있지 않다면
    pos2 = strstr(pos, "/");
    if (pos2 != NULL) {
      *pos2 = '\0'; 
      sscanf(pos, "%s", hostname);
      *pos2 = '/';
      sscanf(pos2, "%s", path);
    } else {
      scanf(pos, "%s", hostname);
    }
  }
  return;
}

/* 캐시가 처음 생성될 때 초기화 함수 */
void cache_init() {
  cache.cache_num = 0;
  int i;
  /* 공유자원인 각각의 cache데이터에 접근할 때에는 락을 걸어야 하므로 Sem_init을 수행한다. */
    // Sem_init 첫 번째 인자: 초기화할 세마포어의 포인터
    // 두 번째: 0 - 프로세스 하나만(쓰레드들끼리 세마포어 공유), 그 외 - 프로세스 간 공유
    // 세 번째: 초기 값(최대 자원) 만약 1이라면 뮤텍스(lock, unlock)이다.
  for (i=0; i<CACHE_OBJS_COUNT; i++) {
    cache.cacheobjs[i].LRU = 0;
    cache.cacheobjs[i].isEmpty = 1;

    Sem_init(&cache.cacheobjs[i].wmutex, 0, 1);
    Sem_init(&cache.cacheobjs[i].rdcntmutex, 0, 1);

    cache.cacheobjs[i].readCnt = 0;
  }
}

/* 
 * 해당 캐시의 인덱스를 읽기전에 readCnt를 1증가하고, 만약 첫 번째 reader라면 해당 캐시를 잠금한다(P연산).
 * 만약, 첫 번째 reader가 아닌 상태에서 계속 잠금시킨다면 음수가 되기때문에 이진세마포어가 아니게 된다.
 */
void readerPre(int i) {
  P(&cache.cacheobjs[i].rdcntmutex);
  cache.cacheobjs[i].readCnt++;
  if (cache.cacheobjs[i].readCnt == 1)
    P(&cache.cacheobjs[i].wmutex);
  V(&cache.cacheobjs[i].rdcntmutex);
}

/*
 * 참조하고 나가는 상태이므로, readCnt를 -1 한 후, 만약 자신이 마지막 reader라면, 해당 캐시의 잠금을 푼다(V연산).
 */
void readerAfter(int i) {
  P(&cache.cacheobjs[i].rdcntmutex);
  cache.cacheobjs[i].readCnt--;
  if (cache.cacheobjs[i].readCnt == 0)
    V(&cache.cacheobjs[i].wmutex);
  V(&cache.cacheobjs[i].rdcntmutex);
}

/* 해당 url이 캐시에 저장되어있는지 확인하는 함수 */
int cache_find(char *url) {
  int i;
  for (i=0; i<CACHE_OBJS_COUNT; i++) {
    readerPre(i);
    // 만약 캐시되어있다면 break
    if ((cache.cacheobjs[i].isEmpty == 0) && (strcmp(url, cache.cacheobjs[i].cache_url) == 0))
      break;
    readerAfter(i);
  }
  // 다 찾아봐도 없을 경우에는 -1을 리턴한다.
  if (i >= CACHE_OBJS_COUNT)
    return -1;
  return i;
}

/* 캐시 빈 공간의 인덱스를 반환하는 함수 */
int cache_eviction() {
  int min = LRU_MAGIC_NUMBER;
  int minindex = 0;
  int i;
  for (i=0; i<CACHE_OBJS_COUNT; i++) {
    readerPre(i);

    /* 만약 해당 캐시인덱스가 비어있는 상황이라면 minindex 갱신 후 break */
    if (cache.cacheobjs[i].isEmpty == 1) {
      minindex = i;
      readerAfter(i);
      break;
    }

    if (cache.cacheobjs[i].LRU < min) {
      minindex = i;
      min = cache.cacheobjs[i].LRU;
      readerAfter(i);
      continue;
    }
    readerAfter(i);
  }
  return minindex;
}

/* 쓰기 전에 해당 캐시의 데이터에 접근하는 것을 lock한다. */
void writePre(int i) {
  P(&cache.cacheobjs[i].wmutex);
}

/* 수정했으므로 캐시의 데이터의 접근을 unlock한다. */
void writeAfter(int i) {
  V(&cache.cacheobjs[i].wmutex);
}

/* 자신을 제외한 cache block 들의 LRU를 내려주는 함수. */
void cache_LRU(int index) {
  int i;
  for (i=0; i<index; i++) {
    writePre(i);
    if (cache.cacheobjs[i].isEmpty == 0 && i != index)
      cache.cacheobjs[i].LRU--;
    writeAfter(i);
  }
  i++;
  for (i; i<CACHE_OBJS_COUNT; i++) {
    writePre(i);
    if (cache.cacheobjs[i].isEmpty == 0 && i != index) {
      cache.cacheobjs[i].LRU--;
    }
    writeAfter(i);
  }
}

/* 해당 uri를 캐시에 저장하는 함수 */
void cache_uri(char *uri, char *buf) {
  int i = cache_eviction();
  
  writePre(i);

  strcpy(cache.cacheobjs[i].cache_obj, buf);
  strcpy(cache.cacheobjs[i].cache_url, uri);
  cache.cacheobjs[i].isEmpty = 0;
  cache.cacheobjs[i].LRU = LRU_MAGIC_NUMBER;
  cache_LRU(i);

  writeAfter(i);
}