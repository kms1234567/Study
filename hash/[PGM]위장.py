# https://school.programmers.co.kr/learn/courses/30/lessons/42578

# 모든 종류에 +1 씩 한다음 다 곱한 후, -1을 한 값이 정답. 
# -1을 하는 이유는 아예 안 입는 경우를 빼야하기 때문이다.

from collections import defaultdict
from itertools import combinations
def solution(clothes):
    answer = 1
    dicts = defaultdict(int)
    for name, kind in clothes:
        dicts[kind] += 1

    for i in dicts.values():
        answer *= (i+1)
    return answer - 1

# 22.10.20
from collections import defaultdict
def solution(clothes):
    answer = 1
    clothes_dict = defaultdict(int)
    for _, kind in clothes:
        clothes_dict[kind] += 1
    for key in clothes_dict.keys():
        answer *= (clothes_dict[key]+1)
    return answer - 1