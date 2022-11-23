# https://school.programmers.co.kr/learn/courses/30/lessons/92335
def isPrime(n):
    if n in [0,1]:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if not n % i:
            return False
    return True
    
def changePrime(n, k):
    tmp = ''
    
    q, r = divmod(n, k)
    while q:
        tmp += str(r)
        q, r = divmod(q, k)
    tmp += str(r)
    
    return tmp[-1::-1]

def solution(n, k):
    answer = 0

    prime = changePrime(n,k)
    # 0을 기준으로 나눔
    word = prime.split('0')
    
    for w in word:
        if not w:
            continue
        if isPrime(int(w)):
            answer += 1
    
    return answer
