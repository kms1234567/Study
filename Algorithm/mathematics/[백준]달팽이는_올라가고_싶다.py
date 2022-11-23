# https://www.acmicpc.net/problem/2869

A, B, V = map(int, input().split())

# A-B 값으로 계속 올라가다보면 마지막에는 A만큼 올라갔을 때 끝나는 경우가 있다.
# 그래서 일단은 V-A만큼 올라가는 값을 구한 후,
tmp_V = V-A

# tmp_V값이 A-B(올라갔다가 내려갔다한 길이)를 나누었을 때 나머지가 0이라면
# 그 위치에서 한 번만 올라가면 된다.
# 반면에 나머지가 1이상이라도 있게되면 그 위치에서 두 번 올라가야 한다.
res = (tmp_V // (A-B))

if not (tmp_V%(A-B)):
    res += 1
else:
    res += 2

print(res)