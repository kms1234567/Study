# https://school.programmers.co.kr/learn/courses/30/lessons/42579

from collections import defaultdict
def solution(genres, plays):
    answer = []

    dicts = defaultdict(list)
    
    # zip으로 다양하게 묶기
    for genre, play, i in zip(genres, plays, range(len(plays))):
        dicts[genre].append([play, i])
    
    # lambda 안에 lambda 사용하기
    for key in sorted(list(dicts.keys()), key = lambda x : sum(map(lambda y : y[0], dicts[x])), reverse = True):
        for cnt, data in enumerate(sorted(dicts[key], key = lambda x : (-x[0], x[1]))):
            if cnt < 2:
                answer.append(data[1])
            else:
                break

    return answer

# 22.10.20
from collections import defaultdict
def solution(genres, plays):
    answer = []
    
    dicts = defaultdict(list)
    for g, p, i in zip(genres, plays, range(len(plays))):
        dicts[g].append((p, i))


    for key in sorted(dicts.keys(), key = lambda x : -sum(map(lambda y:y[0], dicts[x]))):
        tmp = [idx for _, idx in sorted(dicts[key], key = lambda x:-x[0])][:2]
        answer += tmp
            
    return answer