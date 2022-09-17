# https://school.programmers.co.kr/learn/courses/30/lessons/17676

def change(s):
    s = s[11:]
    h, m, seconds = s.split(':')
    s, second_infos = seconds.split(' ')
    second_info = second_infos[:len(second_infos)-1]
    
    if int(float(second_info)*1000) > 3000:
        second_info = '3.0'
    
    end = int(h)*60*60*1000 +int(m)*60*1000 + int(float(s)*1000)
    start = end - int(float(second_info)*1000) + 1
    
    return [start, end]

def solution(lines):
    answer = 0
    
    arr_lines = []
    for line in lines:
        arr_lines.append(change(line))
        
    len_lines = len(lines)
    if len_lines == 1 :
        return 1
    
    for i in range(len_lines-1):
        cnt = 1
        for j in range(i+1, len_lines):
            # 기준이 되는 끝자리가 현재 비교중인 시작-1000보다 크다면 1초안에 포함된다.
            if arr_lines[j][0] - 1000 < arr_lines[i][1] :
                cnt += 1

        answer = max(answer, cnt)
    
    return answer