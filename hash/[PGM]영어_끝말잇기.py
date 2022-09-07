# https://school.programmers.co.kr/learn/courses/30/lessons/12981

from collections import defaultdict
def solution(n, words):
    answer = [0, 0]
    dicts = defaultdict(bool)
    
    prev = ''
    for idx, word in enumerate(words):
        if prev and prev[-1] != word[0] or dicts[word]:
            answer[0] = (idx%n)+1
            answer[1] = (idx//n)+1
            break
        
        prev = word
        dicts[word] = True
        
    return answer