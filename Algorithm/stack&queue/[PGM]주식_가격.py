# https://school.programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    last_idx = len(prices)-1
    answer = [0] * (last_idx+1)

    stk = [] # [값, 최대로 남아있을 때 저장될 값]
    for i in range(last_idx, -1,-1):
        while stk and stk[-1][0] > prices[last_idx-i]:
            data = stk.pop()
            answer[last_idx-data[1]] = data[1] - i
        
        stk.append([prices[last_idx-i], i])

    while stk:
        data = stk.pop()
        answer[last_idx-data[1]] = data[1]
        
    return answer

# 22.10.20
def solution(prices):
    answer = [0 for i in range(len(prices))]
    stk = []
    for i in range(len(prices)):
        while stk and prices[stk[-1]] > prices[i]:
            idx = stk.pop()
            answer[idx] = i - idx
        stk.append(i)
    while stk:
        idx = stk.pop()
        answer[idx] = i - idx
    return answer