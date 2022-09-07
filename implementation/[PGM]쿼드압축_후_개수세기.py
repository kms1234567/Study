# https://school.programmers.co.kr/learn/courses/30/lessons/68936

def recursion(arr, n, w, h):
    ans = [0,0]
    target = arr[w][h]
    
    for i in range(w, w+n):
        for j in range(h, h+n):
            if target != arr[i][j]:
                ans = [i+j for i,j in zip(ans,recursion(arr, n//2, w, h))]
                ans = [i+j for i,j in zip(ans,recursion(arr, n//2, w, h + n//2))]
                ans = [i+j for i,j in zip(ans,recursion(arr, n//2, w + n//2, h))]
                ans = [i+j for i,j in zip(ans,recursion(arr, n//2, w + n//2, h + n//2))]
                return ans
            
    return [0,1] if target else [1,0]
    
def solution(arr):
    N = len(arr)
    answer = recursion(arr, N,0,0)
    
    return answer