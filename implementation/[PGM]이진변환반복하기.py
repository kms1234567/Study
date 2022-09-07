# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    answer = [0, 0]
    
    origin_s = len(s)
    cnt = 0
    while s != '1':
        s = s.replace('0', '')
        trans_s = len(s)
        answer[1] += (origin_s - trans_s)

        s = bin(trans_s)[2:]
        origin_s = len(s)
        cnt += 1
        
    answer[0] = cnt
    return answer