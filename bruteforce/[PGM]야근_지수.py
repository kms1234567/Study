# https://school.programmers.co.kr/learn/courses/30/lessons/12927

def solution(n, works):
    if sum(works) <= n:
        return 0
    len_works = len(works)
    works.sort(reverse = True)
    while n:
        n -= 1;works[0] -= 1
        for i in range(1, len_works):
            if not n:
                break
            if works[i] > works[i-1]:
                n -= 1
                works[i] -= 1
      
    return sum([i**2 for i in works])
