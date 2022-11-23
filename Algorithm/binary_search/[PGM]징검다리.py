# https://school.programmers.co.kr/learn/courses/30/lessons/64062#

def bs(target, stones, k):
    cnt = 0
    for stone in stones:
        if cnt >= k:
            break
        
        if stone - target <= 0:
            cnt += 1
        else:
            cnt = 0
    if cnt >= k:
            return False
    return True

def solution(stones, k):
    answer = 0
    
    left = min(stones);right = max(stones)
    while left <= right:
        mid = (left + right) // 2
       
        check = bs(mid, stones, k)

        if check:
            left = mid + 1
        else:
            answer = mid
            right = mid - 1

    return answer