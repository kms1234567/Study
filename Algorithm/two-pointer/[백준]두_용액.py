import sys
N = int(sys.stdin.readline())

nums = list(map(int, input().split()))
nums.sort()

idx_min = 0
idx_max = N-1

res = nums[0] + nums[-1]
ans = [nums[0], nums[-1]]

while True:
    if idx_min >= idx_max:
        break

    tmp = (nums[idx_min]+nums[idx_max])
    if abs(tmp) < abs(res):
        res = tmp
        ans = [nums[idx_min], nums[idx_max]]
    
    if tmp > 0:
        idx_max -= 1
    else:
        idx_min += 1

print(*ans)