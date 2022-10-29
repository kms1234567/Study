N = int(input())

stk = []
for _ in range(N):
    stk.append(int(input()))

stk.sort(reverse = True)
ans = sum(stk)
for i in range(2, len(stk), 3):
    ans -= stk[i]
print(ans)