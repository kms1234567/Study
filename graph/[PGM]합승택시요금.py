# https://school.programmers.co.kr/learn/courses/30/lessons/72413

# 노드 수가 적지때문에 플로이드-워셜로 해당 노드에서 다른 노드로 가는 모든 경우의 수를 구하였다.
def solution(n, s, a, b, fares):
    answer = int(1e9)
    INF = int(1e9)

    distance = [[INF] * (n+1)  for _ in range(n+1)]

    for i in range(1, n+1):
        distance[i][i] = 0
        
    for start, end, cost in fares:
        distance[start][end] = cost
        distance[end][start] = cost
        
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    
    for i in range(n+1):
        answer = min(answer, distance[s][i] + distance[i][a] + distance[i][b])
    
    return answer