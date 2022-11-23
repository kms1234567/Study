# https://school.programmers.co.kr/learn/courses/30/lessons/12940
def gcf(n, m, res=1):
    for i in range(n,0,-1):
        if i == 1:
            break
        if not n%i and not m%i:
            res = gcf(n//i, m//i, res*i)
            break
    return res

def lcm(g, n, m):
    return n//g * m//g * g

def solution(n, m):
    if n > m:
        n,m = m,n
    
    g = gcf(n, m)
    l = lcm(g, n, m)
    return [g,l]