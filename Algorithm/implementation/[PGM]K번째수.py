# https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []

    # 1. array의 i번째 부터 j번째까지 자릅니다.
    for com in commands:
        i = com[0];j = com[1];k = com[2]
        tmp = array[i-1:j]
        # 2. 정렬합니다.
        tmp.sort()
        # 3. 나온 배열의 k번째 숫자를 저장합니다.
        answer.append(tmp[k-1])
        
    return answer