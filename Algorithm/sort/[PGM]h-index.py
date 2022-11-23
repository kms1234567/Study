def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    for i, c in enumerate(citations, start = 1):
        answer = max(answer, min(i, c))
    return answer