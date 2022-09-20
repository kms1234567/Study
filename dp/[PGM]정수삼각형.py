# https://school.programmers.co.kr/learn/courses/30/lessons/43105
def solution(triangle):
    # 왼쪽(i-1, j-1)과 오른쪽(i-1, j)
    len_triangle = len(triangle)
    for i in range(1, len_triangle):
        for j in range(0, i+1):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])

    return max(triangle[-1])