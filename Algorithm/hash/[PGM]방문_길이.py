# https://school.programmers.co.kr/learn/courses/30/lessons/49994


# 깔끔 풀이
def solution(dirs):
    s = set()
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x, y = nx, ny
    return len(s)//2

# dict 풀이
from collections import defaultdict
def move(x, y, d):
    if d == 'U':
        if y+1 <= 5:
            y += 1
    elif d == 'D':
        if y-1 >= -5:
            y -= 1
    elif d == 'L':
        if x-1 >= -5:
            x -= 1
    else:
        if x+1 <= 5:
            x += 1
    return (x, y)

def solution(dirs):
    answer = 0
    x, y = 0, 0
    coord_dict = defaultdict(list)
    
    for d in dirs:
        nx, ny = move(x, y, d)
        key = str([nx, ny])
        if [x,y] not in coord_dict[key] and [x,y] != [nx,ny]:
            coord_dict[key].append([x,y])
            coord_dict[str([x,y])].append([nx, ny])
            answer += 1
        
        x,y = nx,ny
        
    return answer