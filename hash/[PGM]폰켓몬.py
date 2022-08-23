# https://school.programmers.co.kr/learn/courses/30/lessons/1845

from collections import defaultdict
def solution(nums):
    len_nums = len(nums)//2
    nums = set(nums)
    
    dicts = defaultdict(int)
    for num in nums:
        dicts[num] += 1
    
    res = 0
    for val in dicts.values():
        if val:
            res+=1
    
    return len_nums if res>len_nums else res
