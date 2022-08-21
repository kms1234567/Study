# https://school.programmers.co.kr/learn/courses/30/lessons/12906#

from collections import deque
def solution(arr):
    answer = []
    for i in arr:
        if answer and answer[-1] == i:
            continue
        
        answer.append(i)
        
    return answer