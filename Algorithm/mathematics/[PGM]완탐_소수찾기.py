# https://school.programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations
def checkPrime(num):
    if num == 0 or num == 1:
        return False
    elif num == 2 or num == 3:
        return True
    
    for i in range(2, int(num**0.5)+1):
        if not num % i:
            return False
    return True

def solution(numbers):
    answer = []
    len_numbers = len(numbers)
    
    for i in range(1, len_numbers+1):
        num_list = list(set(permutations(numbers, i)))
        for num in num_list:
            num = int(''.join(num))
            if checkPrime(num):
                answer.append(num)

    return len(set(answer))