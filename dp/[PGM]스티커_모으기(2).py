# https://school.programmers.co.kr/learn/courses/30/lessons/12971

def solution(sticker):
    len_sticker = len(sticker)
    
    # 길이가 1이나 2인 경우에는 큰 스티커를 리턴함
    if len_sticker in [1,2]:
        return max(sticker)
    
    # 1번째 스티커를 뗀 경우와 떼지 않은 경우로 나눠서 생각 해야함
    dp = [[sticker[0], 0]] + [[sticker[0], sticker[1]]] + [[0, 0] for _ in range(len_sticker-2)]
    
    for i in range(2, len_sticker):
        dp[i][0] = max(dp[i-2][0] + sticker[i], dp[i-1][0])
        dp[i][1] = max(dp[i-2][1] + sticker[i], dp[i-1][1])
        if i == len_sticker-1:
            dp[i][0] = max(dp[i-2][0], dp[i-1][0])

    return max(dp[-1])