# https://www.acmicpc.net/problem/14888
N = int(input())

nums = list(map(int, input().split()))

operations = list(map(int, input().split()))

# 0(+) 1(-) 2(*) 3(/)
num_min = 10**9
num_max = -10**9
def solution(operations, val, nums):
    
    global num_min,num_max
    if not sum(operations):
        if num_min > val:
            num_min = val
        if num_max < val:
            num_max = val
        return

    if operations[0] >= 1:
        operations[0] -= 1
        tmp = nums.pop(0)
        solution(operations, val+tmp, nums)
        nums.insert(0, tmp)
        operations[0] += 1

    if operations[1] >= 1:
        operations[1] -= 1
        tmp = nums.pop(0)
        solution(operations, val-tmp, nums)
        nums.insert(0, tmp)
        operations[1] += 1

    if operations[2] >= 1:
        operations[2] -= 1
        tmp = nums.pop(0)
        solution(operations, val*tmp, nums)
        nums.insert(0, tmp)
        operations[2] += 1

    if operations[3] >= 1:
        operations[3] -= 1
        tmp = nums.pop(0)
        solution(operations, int(val/tmp), nums)
        nums.insert(0, tmp)
        operations[3] += 1

solution(operations, nums.pop(0), nums)

print(num_max)
print(num_min)