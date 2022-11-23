# https://school.programmers.co.kr/learn/courses/30/lessons/12906#
def solution(arr):
    answer = []
    for i in arr:
        if answer and answer[-1] == i:
            continue
        
        answer.append(i)
        
    return answer

# 22.10.19

# arr의 배열을 처음부터 순회하면서 연속되는 숫자가 아닐 경우 answer에 append하여 해결하였다.
def solution(arr):
    answer = []
    
    for i in range(len(arr)):
        if not answer or answer[-1] != arr[i]:
            answer.append(arr[i])
    
    return answer