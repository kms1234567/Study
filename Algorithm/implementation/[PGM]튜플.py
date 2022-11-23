# https://school.programmers.co.kr/learn/courses/30/lessons/64065

# 수정한 풀이
from collections import defaultdict
def solution(s):
    total_list = [];str_num=''
    s = s[1:len(s)-1]

    for idx, c in enumerate(s):
        if c.isdigit():
            if s[idx+1].isdigit():
                str_num += c
                continue
                
            if str_num:
                str_num+=c
                total_list.append(int(str_num))
                str_num = ''
                continue
                
            total_list.append(int(c))

    dicts=defaultdict(int)       
    for num in total_list:
        dicts[num] += 1

    return list(i[0] for i in sorted(dicts.items(), key = lambda x : -x[1]))

# 원래 풀이
def solution(s):
    answer = []
    
    total_list = []
    s = s[1:len(s)-1]
    
    tmp = [];str_num = ''
    for idx, c in enumerate(s):
        if c.isdigit():
            if s[idx+1].isdigit():
                str_num += c
                continue
                
            if str_num:
                str_num+=c
                tmp.append(int(str_num))
                str_num = ''
                continue
                
            tmp.append(int(c))
        elif c == '}':
            total_list.append(tmp)
            tmp = []
            
    total_list.sort(key = lambda x : len(x))

    for total in total_list:
        for num in answer:
            total.remove(num)
        answer.append(total[0])
         
    return answer