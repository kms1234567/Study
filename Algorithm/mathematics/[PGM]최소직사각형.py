# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    # 명함을 회전하면 가로 세로를 바꿀 수 있으니,
    # 가로, 세로중에 큰값들 중에 가장 큰 값
    # 가로, 세로중에 작은값들 중에 가장 큰 값의 명함이면 모두 수용할 수 있다.
    return max(map(max,sizes)) * max(map(min,sizes))