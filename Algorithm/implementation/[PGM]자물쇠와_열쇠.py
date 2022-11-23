# https://school.programmers.co.kr/learn/courses/30/lessons/60059

def rotate(key, m):
    result = [[0 for _ in range(m)] for _ in range(m)]
    
    for i in range(0, m):
        for j in range(0, m):
            result[i][j] = key[j][m-1-i]
    return result
    
def attach(key, lock, k, l, m):
    for i, a in zip(range(k, k+m), range(0,m)):
        for j, b in zip(range(l, l+m), range(0,m)):
            lock[i][j] += key[a][b]
    return lock

def detach(key, lock, k, l, m):
    for i, a in zip(range(k, k+m), range(0,m)):
        for j, b in zip(range(l, l+m), range(0,m)):
            lock[i][j] -= key[a][b]
    return lock

def check(lock, m, n):
    
    for i in range(m-1, m+n):
        for j in range(m-1, m+n):
            if lock[i][j] != 1:
                return False
            
    return True
    
def solution(key, lock):
    M = len(key)
    N = len(lock)
    
    add_num = M - 1
    lock_num = N*N - sum(sum(lock, []))
    
    add_r = add_num
    add_c = add_num * 2 + N
    
    for i in range(N):
        lock[i] = [0 for _ in range(add_r)] + lock[i] + [0 for _ in range(add_r)]

    lock = [[0 for _ in range(add_c)] for _ in range(add_r)] + lock
    lock = lock + [[0 for _ in range(add_c)] for _ in range(add_r)]
    
    for i in range(0, N+M-1):
        for j in range(0, N+M-1):
            # rotate 4번
            for _ in range(4):
                # rotate -> attach -> check -> detach 
                key = rotate(key, M)
                lock = attach(key, lock, i, j, M)
                if check(lock, M, N-1):
                    return True
                lock = detach(key, lock, i, j, M)
                
    return False