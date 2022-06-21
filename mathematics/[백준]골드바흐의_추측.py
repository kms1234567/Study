import math

T = int(input())

nums = []

for _ in range(T):
    nums.append(int(input()))

# 10000 까지 소수 판별 진행

primes = [True] * 10001
primes[0] = False;primes[1]=False

for i in range(3, 10001):
    if primes[i]:
        for j in range(2, int(math.sqrt(i)+1)):
            if not i % j:
                primes[i] = False
                break
        # 배수 인덱스들도 모두 False로 변경한다.
        k = 2
        while i * k < 10001:
            primes[i*k] = False
            k += 1

# 차이가 가장 작은 소수의 합을 찾아야 하므로, 2를 나눈수부터 찾아나간다.
for num in nums:
    for i in range(num//2,0,-1):
        front = i
        back = num - i

        if primes[front] and primes[back]:
            print(front, back)
            break

