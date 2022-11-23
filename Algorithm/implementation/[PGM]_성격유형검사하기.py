# https://school.programmers.co.kr/learn/courses/30/lessons/118666?language=python3

from collections import defaultdict
def solution(survey, choices):
    answer = ''
    personality = ['R','T','C','F','J','M','A','N']
    dicts = defaultdict(int)
                        
    for str_tmp, score in zip(survey, choices):
        char1 = str_tmp[0]
        char2 = str_tmp[1]
        
        if score < 4:
            dicts[char1] += (4 - score)
        elif score > 4:
            dicts[char2] += (score - 4)
            
    for i in range(0,4):
        first = personality[i*2]
        second = personality[(i*2)+1]
        
        if dicts[first] > dicts[second]:
            answer += first
        elif dicts[first] < dicts[second]:
            answer += second
        else:
            if first < second:
                answer += first
            else:
                answer += second
    
    return answer