N, D = map(int, input().split())

shortcuts = []
for _ in range(N):
    start, end, distance = map(int, input().split())
    shortcuts.append([start,end,distance])

shortcuts.sort(key = lambda x : (x[1]))
roads = [i for i in range(D+1)]

for i in range(1, D+1):
    roads[i] = roads[i-1] + 1
    for s, e, d in shortcuts:
        if i < e:
            break
        elif i == e:
            roads[i] = min(roads[i], roads[s] + d)
print(roads[D])