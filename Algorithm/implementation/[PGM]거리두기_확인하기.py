# https://school.programmers.co.kr/learn/courses/30/lessons/81302

def solution(places):
    answer = []
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for place in places:
        isKeep = True
        for i, r in enumerate(place):
            for j, c in enumerate(r):
                if c == 'P':
                    for k in range(4):
                        nx = dx[k] + i
                        ny = dy[k] + j
                        if 0<=nx<5 and 0<=ny<5 and place[nx][ny] == 'P':
                            isKeep = False
                            break
                    if not isKeep:
                        break
                elif c == 'O':
                    cnt = 0
                    for k in range(4):
                        nx = dx[k] + i
                        ny = dy[k] + j

                        if 0<=nx<5 and 0<=ny<5 and place[nx][ny] == 'P':
                            cnt += 1
                    if cnt >= 2:
                        isKeep = False
                        break  
            if not isKeep:
                break
        
        if isKeep:
            answer.append(1)
        else:
            answer.append(0)
 
    return answer