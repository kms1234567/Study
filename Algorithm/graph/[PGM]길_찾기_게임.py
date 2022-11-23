# https://school.programmers.co.kr/learn/courses/30/lessons/42892



# > 쉽게 푸는 정렬 <
 
# 인덱스를 앞에 붙이고, info 정보와 함께 저장과 동시에 정렬 진행
# [인덱스, (값, 깊이)]  형식 

# nodes = sorted(list(zip(range(1,len(nodeinfo)+1),nodeinfo)),key=lambda x:(-x[1][1],x[1][0])) # 노드 정렬

import sys
sys.setrecursionlimit(10**6)

def preorder(graph, tmp, v):
    # 중 왼 오
    if v == -1:
        return

    tmp.append(v)
    preorder(graph, tmp, graph[v]['left'])
    preorder(graph, tmp, graph[v]['right'])
    
    return tmp
    
def postorder(graph, tmp, v):
    # 왼 오 중
    if v == -1:
        return
    
    postorder(graph, tmp, graph[v]['left'])
    postorder(graph, tmp, graph[v]['right'])
    tmp.append(v)
    
    return tmp

def solution(nodeinfo):
    answer = []
    
    dicts = dict()
    
    # 각 인덱스에 맞게 연결되지 않은 각각의 노드로 초기화
    for idx, val in enumerate(nodeinfo, start = 1):
        dicts[idx] = {'val':val[0], 'left':-1, 'right':-1}
        nodeinfo[idx-1].append(idx)
    
    # 깊이 순서대로 정렬 후, 삽입한다.
    height_list = sorted(nodeinfo, key = lambda x : x[1], reverse = True)

    root_node = height_list[0][2]
    
    for val, _, node in height_list[1:]:
        parent_node = root_node
        insert_node = node
        while True:
            side = ''
            if val > dicts[parent_node]['val']:
                side = 'right'
            else:
                side = 'left'
            
            if dicts[parent_node][side] == -1:
                break
            else:
                parent_node = dicts[parent_node][side]
        dicts[parent_node][side] = insert_node

    pre_list = preorder(dicts, [], root_node)
    post_list = postorder(dicts, [], root_node)
    
    answer.append(pre_list)
    answer.append(post_list)
    
    return answer