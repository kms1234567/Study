# https://school.programmers.co.kr/learn/courses/30/lessons/12946

def hanoi(answer, n, start, mid, end):
    if not n:
        return
    
    hanoi(answer, n-1, start,end,mid)
    answer.append([start, end])
    hanoi(answer, n-1, mid, start, end)

def solution(n):
    answer = []
    hanoi(answer, n, 1, 2, 3)
    return answer