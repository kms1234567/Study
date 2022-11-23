# https://school.programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque
def bfs(beg, tar, words):
    
    dq = deque([[beg, 0]])
    visited = [False] * len(words)

    while dq:
        node, cnt = dq.pop()

        if node == tar:
            return cnt
        
        for idx, word in enumerate(words):
            if node != word and not visited[idx] and check(node, word):
                dq.append([word, cnt+1])
                visited[idx] = True
    
    
def check(a, b):
    cnt = -2
    for i, j in zip(a,b):
        if i != j:
            cnt += 1
        if cnt >= 0:
            return False

    return True

def solution(begin, target, words):
    answer = bfs(begin, target, words)
    if not answer:
        answer= 0
    return answer