# https://school.programmers.co.kr/learn/courses/30/lessons/17677#

from collections import defaultdict
def solution(str1, str2):
    str1 = str1.lower();str2 = str2.lower()
    if str1 == str2:
        return 65536
    cmp1 = defaultdict(int);cmp2 = defaultdict(int)
    
    for i in range(len(str1)-1):
        target = str1[i] + str1[i+1]
        if target.isalpha():
            cmp1[target] += 1
    for i in range(len(str2)-1):
        target = str2[i] + str2[i+1]
        if target.isalpha():
            cmp2[target] += 1
    
    cmp1_key = set(cmp1.keys());cmp2_key = set(cmp2.keys())
    
    unions = cmp1_key.union(cmp2_key)
    intersections = cmp1_key.intersection(cmp2_key)
    
    num_union = 0;num_intersection = 0
    for strs in unions:
        num_union += (max(cmp1[strs], cmp2[strs]))
    for strs in intersections:
        num_intersection += (min(cmp1[strs], cmp2[strs]))

    if not num_intersection:
        return 0 
        
    return int((num_intersection / num_union) * 65536)