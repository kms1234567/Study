# https://school.programmers.co.kr/learn/courses/30/lessons/68645

# 다른 사람 풀이
def solution(n):
    dx=[0,1,-1]
    dy=[1,0,-1]
    
    b=[[0]*i for i in range(1,n+1)]

    x,y=0,0
    num=1
    d=0
    
    while num<=(n+1)*n//2:
        b[y][x]=num
        ny=y+dy[d]
        nx=x+dx[d]
        
        num+=1
        
        if 0<=ny<n and 0<=nx<=ny and b[ny][nx]==0:
            y,x=ny,nx
        else:
            d=(d+1)%3
            y+=dy[d]
            x+=dx[d]
    # 안에있던 리스트와 빈 리스트가 합쳐져서 1차원 배열로 변경됨   
    return sum(b,[])

# 내 풀이
def solution(n):
    answer = [0] * ((n * (n+1)) // 2)
    
    idx = 0;m=0
    while m < n:
        for i in range(0+(2*m), n-m):
            prev = answer[idx]
            idx += i
            answer[idx] = prev+1

        for i in range(1, n-(3*m)):
            prev = answer[idx]
            idx += 1
            answer[idx] = prev + 1
        
        for i in range(0, n-2-(3*m)):
            prev = answer[idx]
            idx -= (n-m-i)
            answer[idx] = prev + 1
        m += 1
    return answer