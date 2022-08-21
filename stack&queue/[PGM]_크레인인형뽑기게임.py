# https://school.programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    stk = []
    size = len(board)
    moves = [i-1 for i in moves]
    
    for move in moves:
        # 아예 없을 경우
        if board[-1][move] == 0:
            continue
            
        # 뽑아야 할 애는 board[idx_column][move]
        for c in range(0, size):
            idx_column = -1-c
            if idx_column-1 >= -size and board[idx_column-1][move] == 0:
                break
        
        target = board[idx_column][move]
        board[idx_column][move] = 0
        if stk and stk[-1] == target:
            stk.pop()
            answer += 2
            continue
        else:
            stk.append(target)
            
    return answer