# https://school.programmers.co.kr/learn/courses/30/lessons/17684


# 깔끔한 풀이

def solution(msg):
    answer = []
    tmp = {chr(e + 64): e for e in range(1, 27)}
    num = 27
    while msg:
        tt = 1
        while msg[:tt] in tmp.keys() and tt <= msg.__len__():
            tt += 1
        tt -= 1
        if msg[:tt] in tmp.keys():
            answer.append(tmp[msg[:tt]])
            tmp[msg[:tt + 1]] = num
            num += 1
        msg = msg[tt:]
    return answer



from collections import defaultdict
def solution(msg):
    answer = []
    dicts = defaultdict(int)
    for i in range(1,27):
        dicts[chr(i+64)] = i
    len_dicts = len(dicts.keys())
    len_msg = len(msg)
    cnt = 0
    for i in range(len_msg):
        if cnt > 1:
            cnt -= 1
            continue
        cnt = 0
        ans = ''
        while i+cnt < len_msg and dicts[ans+msg[i+cnt]]:
            ans = ans+msg[i+cnt]
            cnt += 1
        answer.append(dicts[ans])
        len_dicts += 1
        if i+cnt < len_msg:
            dicts[ans+msg[i+cnt]] = len_dicts
    return answer