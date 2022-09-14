# https://school.programmers.co.kr/learn/courses/30/lessons/12920

# 1. 시간을 기준으로 이분 탐색을 진행한다.
# 2. 코어의 길이 + 해당 시간에 각 코어의 값을 나눈 몫의 값이 지금까지 작업한 코어들의 개수.
# 3. mid값의 총 작업수(works)가 타겟 작업수인 n 보다 크거나 같은 지점을 찾는 것이 목표. 즉,  'n보다 큰 값 중 가장 작은 값'을 구하는 것
# 4. 해당 값을 구했다면 그것보다 1 뺀 시간에서 나오는 합을 n에서 빼준다.
# 5. 그 후 원래 시간(right)에서 남은 n이 0이 될 때 까지 전진해가면서 인덱스를 찾는다.

def solution(n, cores):
    answer = 0
    
    len_cores = len(cores)
    if n <= len_cores:
        return len_cores
    
    n -= len_cores
    
    left = 0;right = 10000 * len_cores
    
    while left < right:
        mid = (left + right)//2
        
        works = 0
        for c in cores:
            works += (mid // c)
            
        if works >= n:
            right = mid
        else:
            left = mid + 1
    
    for c in cores:
        n -= ((right - 1) // c)
    
    for i in range(len_cores):
        if not right % cores[i]:
            n -= 1
            if not n:
                answer = (i+1)
                break
            
    return answer