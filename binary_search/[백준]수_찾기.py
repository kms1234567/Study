def bns(target, mid):
    if nums[mid] < target:
        return 0
    elif nums[mid] > target:
        return 1
    else:
        return 2


N = int(input())
nums = list(map(int ,input().split()))

M = int(input())
check_nums = list(map(int, input().split()))

nums.sort()

for target in check_nums:
    p = 0
    q = N-1
    while True:
        if p > q:
            print(0)
            break
        
        mid = (p+q) // 2

        is_answer = bns(target, mid)

        if is_answer == 0:
            p = mid + 1
        elif is_answer == 1:
            q = mid - 1
        else:
            print(1)
            break