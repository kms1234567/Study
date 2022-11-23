# https://school.programmers.co.kr/learn/courses/30/lessons/42889

# 부동소수점 대소비교가 파이썬에서 잘 되어있다.. 다른 언어에서도 잘되나? for문에서는 쓰면 안됨!
def solution(N, stages):
    res = [0] * (N+2)
    max_stage = N+1
    denominator = len(stages)
    
    for stage in stages:
        res[stage] += 1
    
    answer = []
    for idx, r in enumerate(res[1:max_stage], start = 1):
        if not r:
            answer.append((0, idx))
            continue
        answer.append((r / denominator, idx))
        denominator -= r
    
    ans = sorted(answer, key = lambda x : (-x[0],x[1]))

    return [i[1] for i in ans]