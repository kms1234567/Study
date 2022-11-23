# https://school.programmers.co.kr/learn/courses/30/lessons/12900#

import sys
sys.setrecursionlimit(10**9)
dp = [1,1] + [0] * 60000
def fibonacci(n):
    if dp[n]:
        return dp[n]
    dp[n] = (fibonacci(n-2) + fibonacci(n-1)) % 1000000007
    return dp[n]
 
def solution(n):
    return fibonacci(n) % 1000000007
