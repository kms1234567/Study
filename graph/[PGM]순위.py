# https://school.programmers.co.kr/learn/courses/30/lessons/49191


# 깔끔풀이
from collections import defaultdict
def solution(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)
    for result in results:
            lose[result[1]].add(result[0])
            win[result[0]].add(result[1])

    for i in range(1, n + 1):
        for winner in lose[i]: win[winner].update(win[i])
        for loser in win[i]: lose[loser].update(lose[i])

    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n - 1: answer += 1
    return answer



from collections import defaultdict
def dfs(win_dicts, start, visited, tmp):
    
    for node in win_dicts[start]:
        if not visited[node]:
            visited[node] = True
            tmp.add(node)
            dfs(win_dicts, node, visited, tmp)
    
def solution(n, results):
    answer = 0
    
    lose_dicts = defaultdict(set)
    win_dicts = defaultdict(set)
    
    lose_ans = defaultdict(set)
    win_ans = defaultdict(set)
    
    list_key = [i for i in range(1, n+1)]
    
    for w, l in results:
        lose_dicts[l].add(w)
        win_dicts[w].add(l)

    for key in list_key:
        tmp = set()
        visited = [False] * (n+1)
        visited[key] = True
        dfs(win_dicts, key, visited, tmp)
        win_ans[key] = win_ans[key].union(tmp)
        
    for key in list_key:
        tmp = set()
        visited = [False] * (n+1)
        visited[key] = True
        dfs(lose_dicts, key, visited, tmp)
        lose_ans[key] = lose_ans[key].union(tmp)
    

    for key in list_key:
        if len(win_ans[key].union(lose_ans[key])) == n-1:
            answer += 1  
    
    return answer