# https://school.programmers.co.kr/learn/courses/30/lessons/12905

# dp 이용하여 풀이하기
def solution(board):
    ans = 0

    row = len(board)
    col = len(board[0])
    
    for r in range(row):
        for c in range(col):
            if not r or not c or not board[r][c]:
                ans = max(ans,board[r][c])
                continue
            board[r][c] = min(board[r-1][c], board[r][c-1], board[r-1][c-1]) + 1
            ans = max(ans, board[r][c])

    return ans*ans

# 시간초과
def check(board, length, r, c):
    for i in range(r, r+length):
        for j in range(c, c+length):
            if not board[i][j]:
                return False
    return True

def solution(board):
    ans = 0
    
    row = len(board)
    col = len(board[0])

    for c in range(col):
        if ans >= col+1-c:
            break
        cnt = 0
        for r in range(row):
            if board[r][c]:
                cnt += 1
                
            if cnt > ans and 0<=c+cnt<=col:
                if check(board, cnt, r-cnt+1, c):
                    ans = cnt
                else:
                    cnt -= 1
            
    return ans**2