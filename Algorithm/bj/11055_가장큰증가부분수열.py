N = int(input())

sequence = list(map(int, input().split()))

ans_list = [sequence[i] for i in range(N)]

# 자기보다 작은 숫자인 인덱스의 최대값 + 자신의 숫자 와 현재 최대값을 비교해서 갱신한다.
for i in range(N):
    for j in range(0, i):
        if sequence[j] < sequence[i]:
            ans_list[i] = max(ans_list[i], sequence[i] + ans_list[j])
print(max(ans_list))