# https://school.programmers.co.kr/learn/courses/30/lessons/12907

# 풀이 방법

# 어떤 방식으로 거스름돈이 구성됐는지는 중요하지 않고, 가짓수만 중요함.
# dp에는 해당 인덱스(가격)까지 몇 개의 경우의 수가 있는지가 기록되어있음.

# 즉, [1,2]원 동전으로 4원을 만드는 방법의 수는
# 1원 동전만으로 4원을 만드는 방법의 수 + 1원 동전만으로 (4-2)원을 만드는 방법의 수 로 구할 수 있다.

def solution(n, money):
    dp = [1] + [0] * n
    
    for coin in money:
        for price in range(coin, n+1):
            if price >= coin:
                  dp[price] += dp[price-coin]
    
    return dp[-1]

