/* $begin tinymain */
/*
 * tiny.c - A simple, iterative HTTP/1.0 Web server that uses the
 *     GET method to serve static and dynamic content.
 *
 * Updated 11/2019 droh
 *   - Fixed sprintf() aliasing issue in serve_static(), and clienterror().
 */
#include "csapp.h"

void doit(int fd);
void read_requesthdrs(rio_t *rp);
int parse_uri(char *uri, char *filename, char *cgiargs);
void serve_static(int fd, char *filename, int filesize);
void get_filetype(char *filename, char *filetype);
void serve_dynamic(int fd, char *filename, char *cgiargs);
void clienterror(int fd, char *cause, char *errnum, char *shortmsg,
                 char *longmsg);

/* Open_listenfd(port)를 통해 listenfd(듣기식별자)를 리턴받는다.
 * Accept(listenfd, sockaddr로 캐스팅한 clientaddr 구조체 주소값, <- 인자값의 길이)를 통해 연결을 시도하여 성공한다면 연결 디스크립터를 리턴한다.
 * Getnameinfo를 통해 주소에 대응되는 (여기서는 클라이언트 구조체의 주소값) 호스트이름과 서비스이름 (스트링) 리턴한다. 
 * 연결 디스크립터를 인자로 doit()함수를 호출하여 트랜잭션을 수행한다.
 */
/* port 번호를 인자로 받는다. */
int main(int argc, char **argv) {
  int listenfd, connfd;
  char hostname[MAXLINE], port[MAXLINE];
  socklen_t clientlen;
  struct sockaddr_storage clientaddr;  // 클라이언트에서 연결 요청을 보내면 알 수 있는 클라이언트 연결 소켓 주소

  /* Check command line args */
  if (argc != 2) {
    fprintf(stderr, "usage: %s <port>\n", argv[0]);
    exit(1);
  }

  /* 해당 포트 번호에 해당하는 듣기 소켓 식별자를 열어준다. */
  listenfd = Open_listenfd(argv[1]);
  
  /* 클라이언트의 요청이 올 때마다 새로 연결 소켓을 만들어 doit() 호출*/
  while (1) {
    /* 클라이언트에게서 받은 연결 요청을 accept한다. connfd = 서버 연결 식별자 */
    clientlen = sizeof(clientaddr);
    connfd = Accept(listenfd, (SA *)&clientaddr, &clientlen);  // line:netp:tiny:accept
    
    /* 연결이 성공했다는 메세지를 위해. Getnameinfo를 호출하면서 hostname과 port가 채워진다. */
    Getnameinfo((SA *)&clientaddr, clientlen, hostname, MAXLINE, port, MAXLINE, 0);
    printf("Accepted connection from (%s, %s)\n", hostname, port);

    /* doit 함수를 실행! */
    doit(connfd);   // line:netp:tiny:doit

    /* 서버 연결 식별자를 닫아준다. */
    Close(connfd);  // line:netp:tiny:close
  }
}

void doit(int fd)
{
  int is_static;
  struct stat sbuf;
  char buf[MAXLINE], method[MAXLINE], uri[MAXLINE], version[MAXLINE];  // 클라이언트에게서 받은 요청(rio)으로 채워진다.
  char filename[MAXLINE], cgiargs[MAXLINE];  // parse_uri를 통해 채워진다.
  rio_t rio;

  Rio_readinitb(&rio, fd);              // 인자로 받은 파일 디스크립터를 rio_t 타입의 읽기 버퍼(&rio)와 연결한다. 
  Rio_readlineb(&rio, buf, MAXLINE);    // 읽기 버퍼에서 한 라인을 읽고, 메모리 위치 buf로 복사한다. (최대 MAXLINE - 1) -> 요청 라인을 읽어들임
  printf("Request headers: \n");
  printf("%s", buf);
  sscanf(buf, "%s %s %s", method, uri, version); // buf 에서 첫 세개 문자열을 읽어온 후, method, uri, version 변수에 저장한다.
  if (strcasecmp(method, "GET")){       // Tiny 서버는 GET요청만 받아들인다.
    clienterror(fd, method, "501", "Not implemented", "Tiny does not implement this method");
    return;
  }
  read_requesthdrs(&rio);               // 다른 헤더들은 읽고 무시한다. (buf에서 비우는 용도)

  /* Parse URI from GET request */
  /* static content이면 is_static = 1, dynamic content이면 is_static = 0 */
  is_static = parse_uri(uri, filename, cgiargs);
  if (stat(filename, &sbuf) < 0){   /* filename(파일)의 모든 정보를 읽고 sbuf에 저장한다. 성공시 0을 반환, 실패 및 에러시 -1을 반환 */
    clienterror(fd, filename, "404", "Not found", "Tiny couldn`t find this file");

    return;
  }

  if (is_static) {  /* Serve static content */
    /* 일반 파일이 아니거나 읽기 권한이 소유자에게 없으면 */
    if (!(S_ISREG(sbuf.st_mode)) || !(S_IRUSR & sbuf.st_mode)) { /* sbuf.st_mode는 파일의 형식과 접근 권한을 의미한다. */
      clienterror(fd, filename, "403", "Forbidden", "Tiny couldn`t read the file");
      return;
    }
    /* serve_static(연결디스크립터, 파일이름, 파일크기의 인자) */
    serve_static(fd, filename, sbuf.st_size); 
  }
  else { /* Serve dynamic content */
    /* 일반 파일이 아니거나 실행 권한이 소유자에게 없으면 */
    if (!(S_ISREG(sbuf.st_mode)) || !(S_IXUSR & sbuf.st_mode)){ 
      clienterror(fd, filename, "403", "Forbidden", "Tiny couldn`t run the CGI program");
      return;      
    }
    serve_dynamic(fd, filename, cgiargs);
  }
}

/* Tiny는 시작줄 외에 요청 헤더 내의 어떤 정보도 사용하지 않으므로, 이들을 읽고 무시한다. */
void read_requesthdrs(rio_t *rp)
{
  char buf[MAXLINE];

  Rio_readlineb(rp, buf, MAXLINE);
  while(strcmp(buf, "\r\n")){   /* HTTP 요청 헤더의 맨 마지막 라인은 "\r\n"으로만 구성되어 있다. (참고로 각 라인마다 "\r\n"이 삽입되어 있다.) */
    Rio_readlineb(rp, buf, MAXLINE);
    printf("%s", buf);
  }
  return;
}

/* 실행파일의 홈 디렉토리는 /cgi-bin 이라고 가정한다. 스트링 cgi-bin을 포함하는 모든 URI는 동적 컨테츠를 요청하는 것을 나타낸다고 가정한다. */
/* 1을 리턴하면 static content, 0을 리턴하면 dynamic content라고 가정한다. */
int parse_uri(char *uri, char *filename, char *cgiargs){
  char *ptr;
  if (!strstr(uri, "cgi-bin")){       /* uri에 "cgi-bin"이 없으면 NULL 리턴 -> Static content */  
    strcpy(cgiargs, "");              /* strcpy(dest, src) : src의 문자열 dest에 복사한다. */
    strcpy(filename, ".");
    strcat(filename, uri);            /* strcat(dest, src) : dest뒤에 src를 붙임. */
    if (uri[strlen(uri)-1] == '/')
      strcat(filename, "home.html");
    return 1;
  }
  else{     /* dynamic content */
    ptr = index(uri, '?');            /* '?' 글자의 주소를 가리킨다. */
    if (ptr){
      strcpy(cgiargs, ptr+1);         /* '?' 글자의 다음 주소를 가리킨다. */
      *ptr = '\0';                    /* '?' 글자 부분에 NULL을 삽입한다. */
    }
    else    /* 인자가 아무것도 없으면 static content와 다를 바 없도록 생성 */
      strcpy(cgiargs, "");
    strcpy(filename, ".");
    strcat(filename, uri);
    return 0;
  }
}

/* 
 * serve_static : 정적데이터들을 서버에서 클라이언트로 옮기는 함수
 * void* mmap(void *addr, size_t len, int prot, int flags, int fd, off_t offset);
 * 파일식별자 fd가 가리키는 객체를 파일에서 offset 바이트 지점을 기준으로 len 바이트만큼 메모리에 맵핑하도록 커널에 요청한다.
 * addr을 넘길 경우, 메모리에서 해당 시작 주소를 선호한다고 커널에게 알린다(보통 0을 넣어서 커널에서 선택하도록 하는 것이 권장된다). 
 * 접근 권한은 prot에 지정하고, 추가동작은 flags에 지정한다. 리턴값은 맵핑의 시작 주소를 반환한다.
 * munmap(void* start, size_t length) 함수는 mmap()함수에 의해 반환된 주소와 해당 길이를 인자로 받아 맵핑을 제거하기 위한 함수이다.
 * malloc은 기본적으로 heap에 저장하며, 공간이 부족할 시 mmap()을 호출(가상메모리)한다.
 */
void serve_static(int fd, char *filename, int filesize)
{
  int srcfd;
  char *srcp, filetype[MAXLINE], buf[MAXBUF];

  /* Send response headers to client 클라이언트에게 응답 헤더 보내기*/
  /* 응답 라인과 헤더 작성 */
  get_filetype(filename, filetype);  // 파일 타입 찾아오기 
  sprintf(buf, "HTTP/1.0 200 OK\r\n");  // 응답 라인 작성
  sprintf(buf, "%sServer: Tiny Web Server\r\n", buf);  // 응답 헤더 작성
  sprintf(buf, "%sConnection: close\r\n", buf);
  sprintf(buf, "%sContent-length: %d\r\n", buf, filesize);
  sprintf(buf, "%sContent-type: %s\r\n\r\n", buf, filetype);
  
  /* 응답 라인과 헤더를 클라이언트에게 보냄 */
  Rio_writen(fd, buf, strlen(buf));  // connfd를 통해 client에게 보냄
  printf("Response headers:\n");
  printf("%s", buf);  // 서버 측에서도 출력한다.

  /************* 11.9 ***************/
  /* Send response body to client */
  srcfd = Open(filename, O_RDONLY, 0); // filename의 이름을 갖는 파일을 읽기 권한으로 불러온다.
  srcp = (char*)Malloc(filesize);
  Rio_readn(srcfd, srcp, filesize);    // 불러온 파일(srcfd)을 srcp에 저장한다.
  Close(srcfd); // 파일을 닫는다.
  Rio_writen(fd, srcp, filesize);  // 해당 메모리에 있는 파일 내용들을 fd(connfd)에 보낸다.
  free(srcp);
}

/* filename에서 filetype을 가져오는 함수 */
void get_filetype(char *filename, char *filetype)
{
  if (strstr(filename, ".html")) /* filename에 해당문자열로 시작하는 부분의 주소(포인터)를 반환한다. */
    strcpy(filetype, "text/html");
  else if (strstr(filename, ".gif"))
    strcpy(filetype, "image/gif");
  else if (strstr(filename, ".png"))
    strcpy(filetype, "image/png");
  else if (strstr(filename, ".jpg"))
    strcpy(filetype, "image/jpeg");
  else if (strstr(filename, ".mpg"))
    strcpy(filetype, "video/mepg");
  else
    strcpy(filetype, "text/plain");
}

/*
 * serve_dynamic : 동적데이터들은 서버에서 클라이언트로 옮기는 함수
 */
void serve_dynamic(int fd, char *filename, char *cgiargs)
{
  char buf[MAXLINE], *emptylist[] = {NULL};

  /* Return first part of HTTP response */
  sprintf(buf, "HTTP/1.0 200 OK\r\n");
  Rio_writen(fd, buf, strlen(buf));
  sprintf(buf, "Server: Tiny Web Server\r\n");
  Rio_writen(fd, buf, strlen(buf));

  if (Fork() == 0) { /* Child */
  /* setenv(char* name, char* value, int rewrite) value값을 가지는 name의 환경변수를 rewrite가 1이므로 이미 환경변수가 존재할 시 새로운 값으로 변경한다.  */
    setenv("QUERY_STRING", cgiargs, 1);
    Dup2(fd, STDOUT_FILENO);  /* 표준 출력을 인자로받은 fd에 의해 복사된다. 자식 프로세스의 표준출력은 fd로 연결됨. */
    Execve(filename, emptylist, environ);   /* 해당 프로그램을 실행한다. */
  }
  Wait(NULL); /* 부모 프로세스는 자식 프로세스가 끝날 때까지 기다린다. */
}

/* TINY clienterror 에러 메시지를 클라이언트에게 보낸다. */
/* HTTP응답을 응답 라인에 적절한 상태 코드와 상태 메시지와 함께 클라이언트에 보내며, 브라우저 사용자에게 에러를 설명하는 HTML 파일도 함께 보낸다. */
void clienterror(int fd, char *cause, char *errnum, char *shortmsg,
                 char *longmsg)
{
  char buf[MAXLINE], body[MAXBUF];
  /* HTTP response body를 생성한다. HTML 응답은 컨텐츠의 크기와 타입을 나타내야 한다. */
  /* sprintf(body, string fomat, args...) : 서식(format)을 지정하여 완성된 문자열을 body에 저장한다. */
  sprintf(body, "<html><title>Tiny Error</title>");
  sprintf(body, "%s<body bgcolor=""ffffff"">\r\n", body);
  sprintf(body, "%s%s: %s\r\n", body, errnum, shortmsg);
  sprintf(body, "%s<p>%s: %s\r\n", body, longmsg, cause);
  sprintf(body, "%s<hr><em>The Tiny Web server</em>\r\n", body);

  /* HTTP 응답을 출력한다. */
  sprintf(buf, "HTTP/1.0 %s %s\r\n", errnum, shortmsg);
  Rio_writen(fd, buf, strlen(buf));
  sprintf(buf, "Content-type: text/html\r\n");
  Rio_writen(fd, buf, strlen(buf));
  sprintf(buf, "Content-length: %d\r\n\r\n", (int)strlen(body));
  Rio_writen(fd, buf, strlen(buf));
  Rio_writen(fd, body, strlen(body));
}