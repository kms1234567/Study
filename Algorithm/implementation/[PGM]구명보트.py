# https://school.programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    answer = 0
    
    people.sort()
    
    front = 0
    end = len(people) - 1
    
    while front < end:
        if people[front] + people[end] <= limit:
            front += 1
            end -= 1
        else:
            end -= 1
        answer += 1
        
    if front == end:
        answer += 1
    
    return answer