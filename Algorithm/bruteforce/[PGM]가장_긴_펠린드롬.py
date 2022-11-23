# https://school.programmers.co.kr/learn/courses/30/lessons/12904


# 1. 현재위치를 왼쪽 기준과 내 오른쪽위치를 기준으로 함께 늘려나가서 개수 세는 방법
# 2. 나를 제외한 내 왼쪽과 오른쪽위치를 기준으로 함께 늘려나가서 개수 세는 방법
def oddString(idx, s, len_s):
    ans = 1
    
    start = idx - 1
    end = idx + 1
    
    while 0 <= start and end < len_s:
        if s[start] == s[end]:
            ans += 2
            start -= 1
            end += 1
        else:
            break
    return ans

def evenString(idx, s, len_s):
    ans = 0
    start = idx
    end = idx + 1
    
    while 0 <= start and end < len_s:
        if s[start] == s[end]:
            ans += 2
            start -= 1
            end += 1
        else:
            break
    return ans

def solution(s):
    answer = 1
    len_string = len(s)
    
    for i in range(len_string):
        answer = max(answer, oddString(i, s, len_string), evenString(i, s, len_string))

    return answer