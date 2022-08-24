# https://school.programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    answer = []
    
    for data in zip(arr1,arr2):
        x = data[0]
        y = data[1]
        
        tmp = []
        for i, j in zip(x,y):
            tmp.append(i+j)
        answer.append(tmp)
        
    return answer