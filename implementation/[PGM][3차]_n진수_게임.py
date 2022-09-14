# https://school.programmers.co.kr/learn/courses/30/lessons/17687


dicts = list('0123456789ABCDEF')
def change(num, n):
    tmp = ''
    
    q, r = divmod(num, n)
    while q:
        tmp += dicts[r]
        q, r = divmod(q, n)
    tmp += dicts[r]
    
    return tmp[-1::-1]
    
def solution(n, t, m, p):
    answer = ''
    
    for i in range(t*m):
        answer += change(i, n)

    return answer[p-1:t*m:m]