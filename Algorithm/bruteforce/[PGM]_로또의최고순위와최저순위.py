# https://school.programmers.co.kr/learn/courses/30/lessons/77484#fn1

def solution(lottos, win_nums):
    cnt = 0;zero_cnt = 0
    for i in lottos:
        if i == 0:
            zero_cnt += 1
            continue
            
        if i in win_nums:
            cnt += 1
            continue

    luck = 7- (cnt + zero_cnt)
    unluck = 7 - cnt

    if luck == 7:
        luck = 6
    if unluck == 7:
        unluck = 6
        
    return [luck,unluck]