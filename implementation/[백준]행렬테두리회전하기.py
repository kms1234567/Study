# https://school.programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows, columns, queries):
    answer = []
    
    boards = []
    for i in range(rows):
        temp = []
        for j in range(1, columns+1):
            temp.append(i*columns + j)
        boards.append(temp)

    for x1, y1, x2, y2 in queries:
        tmp = []
        min_num = 100 * 100
        x1-=1;y1-=1;x2-=1;y2-=1
        
        # 1. x1, y1을 y2까지
        for i in range(y1, y2):
            tmp.append((x1, i))
        # 2. x1을 x2까지, y2
        for i in range(x1, x2):
            tmp.append((i,y2))
        # 3. x2, y2를 y1까지
        for i in range(y2, y1, -1):
            tmp.append((x2,i))
        # 4. x2를 x1까지, y1
        for i in range(x2, x1, -1):
            tmp.append((i,y1))
        
        pre = boards[tmp[-1][0]][tmp[-1][1]]
        for i in range(len(tmp)):
            x = tmp[i][0];y = tmp[i][1]
            min_num = min(min_num, boards[x][y])
            
            tmp_val = boards[x][y]
            boards[x][y] = pre
            pre = tmp_val
            
        answer.append(min_num)
             
    return answer