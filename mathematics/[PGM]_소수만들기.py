# https://school.programmers.co.kr/learn/courses/30/lessons/12977

from math import sqrt
def prime_check(num):
    for n in range(2, int(sqrt(num))+1):
        if num % n == 0:
            return False
    return True

def solution(nums):
    nums_len = len(nums)
    cnt = 0
    
    for i in range(0, nums_len-2):
        for j in range(i+1, nums_len-1):
            for k in range(j+1, nums_len):
                target = nums[i] + nums[j] + nums[k]
                
                if prime_check(target):
                    cnt += 1

    return cnt