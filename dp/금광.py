for _ in range(int(input())):
    n, m = map(int, input().split())

    inputs = list(map(int, input().split()))
    mines = []
    for i in range(1, n+1):
        mines.append(inputs[(i-1)*m:i*m])
    
    for j in range(1,m):
        for i in range(n):
            if i == 0:
                mines[i][j] = mines[i][j] + max(mines[i][j-1], mines[i+1][j-1])
            elif i == n-1:
                mines[i][j] = mines[i][j] + max(mines[i][j-1], mines[i-1][j-1])
            else:
                mines[i][j] = mines[i][j] + max(mines[i][j-1], mines[i-1][j-1], mines[i+1][j-1])

    max_val = 0
    for i in range(n):
        max_val = max(max_val, mines[i][m-1])
    print(max_val)