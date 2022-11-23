n, k = map(int, input().split())

thing = [[0,0]]
d = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    thing.append(list(map(int, input().split())))

# bottom_up 방식
# 행(i)은 물품 수를 의미하며, 열(k)은 물품의 무게를 의미한다.
for i in range(1, n+1):
    for j in range(1, k+1):
        w = thing[i][0]
        v = thing[i][1]

        # 해당 물건은 현재 들어갈 수 있는 가방 무게를 초과해을 경우, 위 행값을 가져옴
        if j < w:
            d[i][j] = d[i-1][j]
        # 들어갈 수 있다면, 위행(현재 물건이 들어가지 않는)과 해당 물건을 뺏을 때의 최대값 + 현재 물건값 중 최대값을 넣게 된다.
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)

print(d[n][k])