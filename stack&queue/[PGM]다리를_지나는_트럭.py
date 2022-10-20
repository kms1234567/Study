# https://school.programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque
def solution(bridge_length, weight, truck_wait):
    cnt = 0
    # 3. 1초마다 다리를 건너는 트럭의 합이 < 무게+ 대기중인 첫번째 트럭 일때 하나 넣기
    # 4. 즉, 로직은 1초 증가 -> 다리 트럭있을 경우 시간이 다 됐는지 확인 -> 대기트럭 하나가 다리 건널 수 있는지 로직 
    # 5. 데이터를 넣을 때 나와야될 시간(cnt + bridge_length)도 같이 저장하자.
    truck_wait = deque(truck_wait)
    truck_road = deque()
    
    sum_weight = 0
    while truck_wait:
        cnt += 1
        # 첫 번째 값이 나올 시간이 되었는지 확인 후 빼버림.
        if truck_road and truck_road[0][1] == cnt:
            sum_weight -= truck_road.popleft()[0]
            
        # 대기트럭하나가 다리를 건널 수 있는 무게면, 대기트럭 첫번째 값을 빼고 도로트럭에 넣음.
        if sum_weight + truck_wait[0] <= weight:
            truck = truck_wait.popleft()
            sum_weight += truck
            truck_road.append((truck, cnt+bridge_length))
            
    return truck_road[-1][1]

# 22.10.20
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer, sum_curr = 0, 0
    
    truck_curr = deque()    
    truck_weights = deque(truck_weights)
    
    while truck_weights or truck_curr:
        answer += 1
        
        if truck_curr and (answer - truck_curr[0][0]) >= bridge_length:
            pop_truck = truck_curr.popleft()
            sum_curr -= (pop_truck[1])
            
        if truck_weights and sum_curr + truck_weights[0] <= weight:
            pop_truck = truck_weights.popleft()
            sum_curr += pop_truck
            truck_curr.append([answer, pop_truck])
        
    return answer