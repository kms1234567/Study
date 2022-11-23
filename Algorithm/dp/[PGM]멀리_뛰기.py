# https://school.programmers.co.kr/learn/courses/30/lessons/12914

import sys
sys.setrecursionlimit(10**9)
dp = [1, 1, 2] + [0]*(2000)  
def recursion(n):
    if dp[n]:
        return dp[n]
    
    dp[n] = recursion(n-1) + recursion(n-2)
    return dp[n]
    

def solution(n):
    ans = recursion(n)

    return ans % 1234567


# 시간초과 코드 -> 해당 코드를 통해 규칙성을 찾아냈음
import sys
sys.setrecursionlimit(10**8)
def dfs(li, strings, total, target):
    if total == target:
        li.append(strings)
        return
    elif total>target:
        return
    
    dfs(li, strings+'1', total+1, target)
    dfs(li, strings+'2', total+2, target)


def solution(n):
    answer = 0
    
    noc_list = []
    
    dfs(noc_list, '', 0, n)
    
    return len(set(noc_list))