# https://school.programmers.co.kr/learn/courses/30/lessons/42747#

def solution(citations):
    answer = 0

    len_citation = len(citations)
    citations.sort()
    for i, c in enumerate(citations):
        answer = max(answer,min(len_citation-i, c))
        
    return answer