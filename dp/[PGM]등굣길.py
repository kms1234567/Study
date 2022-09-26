# https://school.programmers.co.kr/learn/courses/30/lessons/42898

# 1. 오른쪽과 아래로밖에 못간다. 모든 배열을 1로 만든 후, 왼쪽과 위쪽을 합해가면서 목적지까지 도달한다.
# 2. 웅덩이는 0으로 만들고, 웅덩이칸에서는 더하지말고 continue 한다.
# 3. 만약 행과 열이 가장 윗칸 혹은 왼쪽이라면 거기서부터 시작해서 오른쪽 혹은 아래쪽 까지는 이용을 못하게 되므로 0으로 만든다.

def solution(m, n, puddles):
    dp = [[1 for _ in range(m)] for _ in range(n)]
    
    for y, x in puddles:
        dp[x-1][y-1] = 0
        if x == 1:
            for i in range(y-1,m):
                dp[x-1][i] = 0
        if y == 1:
            for i in range(x-1, n):
                dp[i][y-1] = 0

    for i in range(0, n):
        for j in range(0, m):
            
            if not dp[i][j]:
                continue
            if i-1 >= 0 and j-1 >= 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[-1][-1] % 1000000007