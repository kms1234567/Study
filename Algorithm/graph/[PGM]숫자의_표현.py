# https://school.programmers.co.kr/learn/courses/30/lessons/12924

import sys
sys.setrecursionlimit(10**8)

def dfs(visited, start, cur, total ,target):
    if visited[start]:
        return
    
    if total == target:
        visited[start] = 1
        return 
    elif total > target:
        visited[start] = 2
        return
    
    dfs(visited, start, cur+1, total+cur, target)
    dfs(visited, cur+1, cur+2, cur+1, target)

def solution(n):
    visited = [0] * (10001)
    dfs(visited, 1, 1, 0, n)
    return sum([i for i in visited if i == 1])