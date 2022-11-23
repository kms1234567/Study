# https://school.programmers.co.kr/learn/courses/30/lessons/12923


def solution(begin, end):
    answer = []
    
    for i in range(begin, end + 1):
        if i == 1:
            answer.append(0)
            continue

        for j in range(2, int(i**0.5)+1):
            share = i // j
            # 데이터에 넣어질 몫이 10,000,000번 블록이 나오면 안 됨.
            if share > 10**7:
                continue
            
            if not i % j:
                answer.append(share)
                break
        else:
            answer.append(1)        
    
    return answer