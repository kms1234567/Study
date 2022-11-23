def dfs(depth=0, talls=[], idx=-1):

    # 7개를 구해야 하므로 depth 제한은 7
    if depth == 7:
        if sum(talls) == 100:
            for i in talls:
                print(i)
            exit(0)
        return
    
    # 총 개수만큼 반복하다가
    for i in range(N):
        # idx보다 크면 append
        if i > idx:
            talls.append(heights[i])
            # depth를 1 증가시켜주고, 똑같은 값을 넣지 않기 위해 idx로 현재 i를 전달
            dfs(depth+1, talls, i)
            # 100이 안돼서 나왔을 경우 pop!
            talls.pop()

heights = []

N = 9

for _ in range(N):
    heights.append(int(input()))

heights.sort()

dfs()