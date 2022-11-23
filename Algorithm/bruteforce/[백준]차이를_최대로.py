from itertools import permutations, combinations
def check(nums):
    # print(nums)
    ret = 0
    for i in range(len(nums)-1):
        ret += abs(nums[i]-nums[i+1])
    return ret

def solution(depth, arr):
    if depth == N:
        res.append(check(arr))
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            arr.append(nums[i])
            solution(depth+1, arr)
            visited[i] = False
            arr.pop()

N = int(input())

nums = list(map(int, input().split()))
visited = [False] * N

res = []

solution(0,[])

print(max(res))