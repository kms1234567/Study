# https://school.programmers.co.kr/learn/courses/30/lessons/17682

# 다른 사람 풀이
import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

# 내 풀이
def solution(dartResult):
    dicts = {'S':'first', 'D':'second', 'T':'third', '':0, 0:0,'first':0,'second':0,'third':0}
    dartResult = str(dartResult) + '0'
    tmp = 0  
    state = '';previous_state = ''
    
    for idx, s in enumerate(dartResult):
        if s.isdigit():
            if s=='1' and dartResult[idx+1] == '0':
                dicts[dicts[state]] += tmp
                tmp = 10
                continue
            if s=='0' and dartResult[idx-1] == '1':
                continue
            dicts[dicts[state]] += tmp
            tmp = int(s)
        elif s.isalpha():
            if s == 'S':
                tmp = tmp ** 1
            elif s == 'D':
                tmp = tmp ** 2
            else:
                tmp = tmp ** 3
            previous_state = state 
            state = s
        else:
            if s == '*':
                tmp *= 2
                dicts[dicts[previous_state]] *= 2
            else:
                tmp *= (-1)
    return dicts['first'] + dicts['second'] + dicts['third']