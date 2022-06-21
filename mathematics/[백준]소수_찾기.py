#https://www.acmicpc.net/problem/1978
import math

# 체크할 수의 배수가 있는지 자신보다 작은 수를 나눈 나머지를 보면서 0인 경우 False를 리턴한다.
# 자신의 제곱근까지만 확인하면 된다는 성질을 이용하여 검사할 수를 줄인다.
# 100의 약수는 (1,100) (2,50) (4,25) (5,20) (10,10), (20,5) (25,4) (50,2) (100,1) 로
# 자신의 제곱근 수 이후로는 반복되는 것을 알 수 있다.
def check_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)+1)):
        if not n % i:
            return False
    return True

N = int(input())

nums = list(map(int, input().split()))

ans = 0

for i in range(N):
    if check_prime(nums[i]):
        ans += 1

print(ans)