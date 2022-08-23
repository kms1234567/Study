# https://school.programmers.co.kr/learn/courses/30/lessons/77884
# 지리는 풀이
def solution(left, right):
    answer = 0
    
    # 애초에 짝수라고 가정
    for num in range(left, right+1):
        if int(num**0.5) == num**0.5:
            answer -= num
        else:
            answer += num
    
    return answer


# 내가 푼 풀이
from math import sqrt
def solution(left, right):
    answer = 0
    
    for num in range(left, right+1):
        cnt = 0
        for i in range(1, int(sqrt(num)) + 1):
            if not num % i:
                if num//i != i:
                    cnt += 2
                else:
                    cnt += 1
        
        if not cnt % 2:
            answer += num
        else:
            answer -= num
    
    return answer