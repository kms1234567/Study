# https://school.programmers.co.kr/learn/challenges?order=recent&levels=2&languages=python3

def solution(n):
    dp = [0, 1] + [0] * (n-1)
    for i in range(2, n+1):
        dp[i] = dp[i-2] + dp[i-1]
    
    return dp[-1] % 1234567