# https://school.programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    answer = []
    K=k

    for idx, num in enumerate(number):
        if not k:
            answer += number[idx:]
            break

        while answer and answer[-1] < num and k:
            answer.pop()
            k -= 1
        answer.append(num)
        
    return ''.join(answer[:len(number)-K])