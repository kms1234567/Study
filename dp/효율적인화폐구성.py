N, M = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

INF = 10001 
dp = [0] + [INF for _ in range(M)]

for i in range(1, M+1):
    for coin in coins:
        if i - coin >= 0:
            dp[i] = min(dp[i], dp[i-coin]+1)

print(dp[M] if dp[M] != INF else -1)