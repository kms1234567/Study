# https://school.programmers.co.kr/learn/courses/30/lessons/42861

# 크루스칼 알고리즘 사용

# -> 모든 간선의 가중치를 작은 순서대로 정렬하고, 작은 간선부터 양 끝의 두 정점을 비교하여 연결하는 알고리즘

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
    
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    
    return parent[x]

def solution(n, costs):
    answer = 0
    
    costs.sort(key = lambda x : x[2])
    parent = [i for i in range(n)]
    
    for s, e, c in costs:
        if not sum(parent):
            break
        # 사이클 방지
        if find(parent, s) != find(parent, e):
            union(parent, s, e)
            answer += c
        else:
            continue

    return answer