# https://school.programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
    if n == 2:
        return 1
    elif n == 3:
        return 2
    
    answer = 2
    
    for i in range(4, n+1):
        for j in range(2, int(i**0.5)+1):
            if not i % j:
                break
        else:
            answer += 1
    
    return answer