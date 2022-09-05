# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []
    sum_by = brown + yellow
    
    # i는 세로 j는 가로
    for i in range(3, int(sum_by**0.5)+1):
        if not sum_by % i:
            j = sum_by // i
            brw = (j*2) + ((i-2)*2) 
            ylw = sum_by - brw
            if brw == brown:
                answer = [j, i]
                break

    return answer