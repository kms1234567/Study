from collections import deque

N, K = map(int, input().split())

path = [0 for _ in range(100001)]
visited = [0 for _ in range(100001)]
def find():
    cur = K
    stk = []
    while cur != N:
        stk.append(cur)
        cur = path[cur]
    stk.append(N)
    stk.reverse()
    print(visited[K])
    print(*stk)

def bfs():
    q = deque()
    q.append(N)

    while q:
        cur = q.popleft()
        if cur == K:
            find()
            break

        for new_node in (cur-1, cur+1, cur*2):
            if 0 <= new_node < 100001 and not path[new_node]:
                q.append(new_node)
                visited[new_node] = visited[cur] + 1
                path[new_node] = cur

bfs()