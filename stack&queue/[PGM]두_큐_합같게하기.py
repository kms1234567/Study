# https://school.programmers.co.kr/learn/courses/30/lessons/118667

# 다른사람 풀이
from collections import deque
def solution(queue1, queue2):
    answer = 0
    
    q1 = deque(queue1);q2 = deque(queue2)
    
    sum_q1 = sum(q1)
    mid = (sum_q1 + sum(q2)) // 2

    while q1 and q2:
        if sum_q1 > mid:
            pop_num = q1.popleft()
            sum_q1 -= pop_num
        elif sum_q1 < mid:
            pop_num = q2.popleft()
            q1.append(pop_num)
            sum_q1 += pop_num
        else:
            return answer
        answer += 1
    
    return -1

# 내 풀이
from collections import deque
def solution(queue1, queue2):
    answer = 0
    
    q1 = deque(queue1);q2 = deque(queue2)
    
    sum_q1 = sum(q1);sum_q2 = sum(q2)
    target_num = (sum_q1 + sum_q2) // 2
    max_cnt = len(q1) * 3
    
    # 그리디하게 큰곳에서 작은곳으로 가도록 하자
    # 현재 어느쪽이 큰지 상태를 지속적으로 저장하자 (q1 q2)
    # 처음에만 sum을쓰고 후에는 연산을 통해 sum을 계속 써서 확인하지 않도록 하자
    # 나와야하는 최대횟수를 정하고, 초과하면 -1을 출력하자
    
    state = 'q1' if sum_q1 > sum_q2 else 'q2'
    
    while sum_q1 != sum_q2 and answer <= max_cnt:
        if state == 'q1':
            pop_num = q1.popleft()
            q2.append(pop_num)
            sum_q1 -= pop_num;sum_q2 += pop_num
        else:
            pop_num = q2.popleft()
            q1.append(pop_num)
            sum_q1 += pop_num;sum_q2 -= pop_num
            
        state = 'q1' if sum_q1 > sum_q2 else 'q2'
        answer += 1
    
    return answer if answer <= max_cnt else -1