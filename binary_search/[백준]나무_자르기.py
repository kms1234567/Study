def bs(mid, M):

    tmp = 0

    for t in trees:
        if t > mid:
            tmp += (t - mid)
    if tmp >= M:
        return True
    else:
        return False

N, M = map(int, input().split())

trees = list(map(int, input().split()))

p = 0
q = 10**9

height = 0
while True:
    if p > q:
        break

    mid = (p+q) // 2

    if bs(mid, M):
        height = mid
        p = mid + 1
    else:

        q = mid - 1

print(height)

    