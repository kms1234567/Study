# https://school.programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    answer = 1
    
    routes.sort(key = lambda x : x[1])
    prev = routes[0][1]
    
    for entry, out in routes[1:]:
        if entry > prev:
            prev = out
            answer += 1
    
    return answer