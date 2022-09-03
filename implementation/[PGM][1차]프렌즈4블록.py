# https://school.programmers.co.kr/learn/courses/30/lessons/17679#

# board의 빈 부분을 아래로 압축시키는 함수
def compressList(m, n, board):
    for y in range(0, n):
        empty_list = []
        for x in range(m-1, -1, -1):
            if not board[x][y]:
                empty_list.append((x,y))
            elif empty_list:
                ex, ey = empty_list.pop(0)
                tmp = board[ex][ey]
                board[ex][ey] = board[x][y]
                board[x][y] = tmp
                empty_list.append((x,y))

# 삭제되어야할 del_list에 좌표를 담음. 없으면 빈 리스트를 반환
def check(m, n, board, del_list):
    for x in range(0, m):
        for y in range(0, n):
            target = board[x][y]
            if not target:
                continue
            if 0<=x+1<m and 0<=y+1<n and target == board[x][y+1] and target == board[x+1][y] and target == board[x+1][y+1]:
                del_list.append((x,y));del_list.append((x,y+1));del_list.append((x+1,y));del_list.append((x+1,y+1))
            
    return list(set(del_list))
            
def solution(m, n, board):
    answer = 0
    
    board = list(map(list,board))
    del_list = check(m, n, board, [])
    while del_list:
        # del_list 만큼 보드 삭제
        for x, y in del_list:
            answer += 1
            board[x][y] = 0
        # board 빈 부분 압축
        compressList(m, n, board)
        # 다시 del_list 담음
        del_list = check(m, n, board, [])

    return answer