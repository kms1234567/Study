X = int(input())

d = [0 for _ in range(30001)]

for i in range(2, X + 1):
    d[i] = d[i-1] + 1

    if not i % 2:
        d[i] = min(d[i], d[i//2] + 1)
    if not i % 3:
        d[i] = min(d[i], d[i//3] + 1)
    if not i % 5:
        d[i] = min(d[i], d[i//5] + 1)

print(d[X])