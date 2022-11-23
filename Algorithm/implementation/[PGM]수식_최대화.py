# https://school.programmers.co.kr/learn/courses/30/lessons/67257/solution_groups?language=python3

# 깔끔풀이
from itertools import permutations
def calc(priority, n, expression):
    if n == 2:
        return str(eval(expression))
    if priority[n] == '*':
        res = eval('*'.join([calc(priority, n + 1, e) for e in expression.split('*')]))
    if priority[n] == '+':
        res = eval('+'.join([calc(priority, n + 1, e) for e in expression.split('+')]))
    if priority[n] == '-':
        res = eval('-'.join([calc(priority, n + 1, e) for e in expression.split('-')]))
    return str(res)


def solution(expression):
    answer = 0
    priorities = (list(permutations(['*','-','+'], 3)))
    for priority in priorities:
        res = int(calc(priority, 0, expression))
        answer = max(answer, abs(res))

    return answer




from itertools import permutations
import re
def solution(expression):
    answer = 0
    dicts = {'*':'\d+\*\-?\d+', '+':'\d+\+\-?\d+', '-':'\-?\d+\-\-?\d+'}
    cases = list(permutations(['*', '+', '-'],3))
    
    for case in cases:
        form = expression
        minus_idx = case.index('-')
        for cur_idx, c in enumerate(case):
            while True:
                ex = dicts[c]
                if minus_idx < cur_idx:
                    ex = '\-?' + ex
                search = re.search(ex, form)
                if not search:
                    break
                num = str(eval(search[0]))
                x, y = search.span()
                form = form[:x] + num + form[y:]

        answer = max(answer, abs(int(eval(form))))        
    
    return answer