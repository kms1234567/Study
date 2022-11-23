# https://school.programmers.co.kr/learn/courses/30/lessons/67258#

from collections import defaultdict 

def solution(gems):
    num = len(set(gems))
    ret = []

    left = 0
    counter = defaultdict(int)
    
    for right in range(len(gems)):
        counter[gems[right]] += 1
        right += 1
        while len(counter) == num:
            counter[gems[left]] -= 1
            if counter[gems[left]] == 0:
                del counter[gems[left]]
            left += 1
            ret.append([left, right])

    return sorted(ret, key = lambda x: (x[1]-x[0], x[0]))[0]