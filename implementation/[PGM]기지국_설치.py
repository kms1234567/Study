# https://school.programmers.co.kr/learn/courses/30/lessons/12979


# stations 배열을 순회하면서 그 전까지 남아있는(전파해야할) 마을들의 개수를 전파 범위(2*w+1)로 나눈 값을 더합니다.
# 만약 나누어떨어지면 추가로 안 더해도 되지만 나머지가 있다면 1을 더 더합니다.

def solution(n, stations, w):
    answer = 0

    # stations 마지막 범위까지 순회하기 위해 마지막 바로 다음까지 전파범위가 닿는 기지국을 임의로 설치합니다.
    stations.append(n+w+1)
    len_stations = len(stations)
    
    station_range = (2*w) + 1
    prev_start = 1
    for i in range(len_stations):
        station = stations[i]
        remain = station - w - prev_start
        
        answer += remain // station_range
        if remain % station_range:
            answer += 1
        
        prev_start = stations[i] + w + 1
        
    return answer