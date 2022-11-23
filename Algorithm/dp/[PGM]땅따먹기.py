# https://school.programmers.co.kr/learn/courses/30/lessons/12913

from copy import deepcopy
def solution(land):
    dp = deepcopy(land)

    for row, data in enumerate(land[1:], start = 1):
        for col, d in enumerate(data):
            if col == 0:
                pre_max = max(dp[row-1][col+1], dp[row-1][col+2], dp[row-1][col+3])
            elif col == 1:
                pre_max = max(dp[row-1][col-1], dp[row-1][col+1], dp[row-1][col+2])
            elif col == 2:
                pre_max = max(dp[row-1][col-2], dp[row-1][col-1], dp[row-1][col+1])
            else:
                pre_max = max(dp[row-1][col-3], dp[row-1][col-2], dp[row-1][col-1])
            dp[row][col] = pre_max + dp[row][col]
    
    return max(dp[-1])