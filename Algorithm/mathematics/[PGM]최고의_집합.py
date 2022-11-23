# https://school.programmers.co.kr/learn/courses/30/lessons/12938

# 1. 가장 큰 합을 만들기 위해서는 모든 숫자들이 중앙에 모여있어야함.
# 2. 나눈 몫으로 먼저 배열을 만듦.
# 3. 나머지 개수만큼 뒤에서부터 1씩 더함.

def solution(n, s):
    answer = []
    if s % n == s:
        return [-1]
    
    x, y = divmod(s, n)
    answer = [x for _ in range(n)]
    
    idx = -1
    while y:
        answer[idx] += 1
        y -= 1;idx -= 1

    return answer