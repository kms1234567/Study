# https://school.programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    answer = []
    
    len_num = len(numbers)
    
    for i in range(0, len_num-1):
        for j in range(i+1, len_num):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))