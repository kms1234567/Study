# https://school.programmers.co.kr/learn/courses/30/lessons/43238#

def bs(target, n, times):
    total = 0
    for time in times:
        total += (target // time)
    
    if total >= n:
        return True
    else:
        return False

def solution(n, times):
    answer = 0
    left = 0;right = 1000000000 * len(times)
    
    while left < right:
        mid = (left + right) // 2
        
        check = bs(mid, n, times)

        if check:
            answer = mid
            right = mid
        else:
            left = mid + 1

    return answer