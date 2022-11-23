# https://www.acmicpc.net/problem/2110
import sys
def bs(mid, C):
    cnt = 1

    prev = modems[0]
    for i in modems[1:]:
        if i - prev >= mid:
            cnt += 1
            prev = i
    
    if cnt >= C:
        return True
    else:
        return False


N, C = map(int, sys.stdin.readline().split())

modems = []

for _ in range(N):
    modems.append(int(sys.stdin.readline()))
modems.sort()

p = 1
q = modems[-1]
res = 0
while True:
    if p > q:
        break

    mid = (p+q)//2

    if bs(mid, C):
        res = max(res,mid)
        p = mid + 1
    else:
        q = mid - 1

print(res)