# https://school.programmers.co.kr/learn/courses/30/lessons/77885

# 정답 풀이
def solution(numbers):
    answer = []
    
    # 짝수일 때는 마지막 비트가 무조건 0이다. -> 마지막 비트를 1 올린 것이 답이므로 +1 한 값이 답
    # 홀수일 때는 마지막 비트가 무조건 1이다. -> 0인 인덱스를 찾음. 해당 0의 인덱스를 1로 변경 후 다음 비트의 1을 0으로변경한 값이 답
    for num in numbers:
        stk = ['0']+list(bin(num)[2:])
        
        if not num % 2:
            answer.append(num+1)
        else:
            for i in range(-1,-len(stk)-1,-1):
                if stk[i] == '0':
                    stk[i] = '1'
                    stk[i+1] = '0'
                    answer.append(int(''.join(stk), 2))
                    break
        
    return answer

# 틀린 풀이

def solution(numbers):
    answer = []
    
    for num in numbers:
        plus = 1
        while True:
            cmp = num+plus
            if str(bin(num^cmp)).count('1') in [1,2]:
                answer.append(num+plus)
                break
            else:
                plus+=1

    return answer