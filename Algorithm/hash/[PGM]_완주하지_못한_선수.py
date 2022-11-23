# https://school.programmers.co.kr/learn/courses/30/lessons/42576

from collections import defaultdict
def solution(participant, completion):
    dicts = defaultdict(int)
    
    for pt_name in participant:
        dicts[pt_name] += 1
        
    for cp_name in completion:
        dicts[cp_name] -= 1

    for key in dicts.keys():
        if dicts[key]:
            return key

# 2022.10.19

# Counter를 이용하여 무조건 하나가 더 많은 participant를 기준으로 많은 값의 key를 반환하도록 했다.

from collections import Counter
def solution(participant, completion):
    counter_participant = Counter(participant)
    counter_completion = Counter(completion)
    
    for key in counter_participant.keys():
        if counter_participant[key] > counter_completion[key]:
            return key