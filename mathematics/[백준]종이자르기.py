# https://www.acmicpc.net/problem/2628
M, N = map(int, input().split())

K = int(input())

# 가로 세로 배열에 값을 모두 담은 후, 정렬한다.
rows = [0, N]
columns = [0, M]

for i in range(K):
    a, b = map(int, input().split())
    if a:
        columns.append(b)
    else:
        rows.append(b)

rows.sort()
columns.sort()

# 나올 수 있는 길이들을 모두 측정후, 각 max값을 곱한 값을 출력한다.
widths = []
heights = []

for w in range(len(rows)-1):
    widths.append(rows[w+1]-rows[w])

for h in range(len(columns)-1):
    heights.append(columns[h+1]-columns[h])

print(max(widths) * max(heights))