# https://school.programmers.co.kr/learn/courses/30/lessons/17686

import re
def solution(files):
    for idx, file in enumerate(files):
        match = re.search('\d+', file)
        head = file[0:match.span()[0]]
        number = match[0]
        
        files[idx] = [file, head, number]
    
    files.sort(key = lambda x : (x[1].lower(), int(x[2])))

    return [file[0] for file in files]