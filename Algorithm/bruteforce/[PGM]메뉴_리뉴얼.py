# https://school.programmers.co.kr/learn/courses/30/lessons/72411

# 깔끔한 풀이...
from itertools import combinations
from collections import defaultdict, Counter


def solution(orders, course):
    result = []
    for i in course:
        menu_dict = defaultdict(int)
        for order in orders:
            for menu in combinations(order, i):
                if len(list(filter(lambda x: x in menu, list(order)))) == len(menu):
                    menu_dict[''.join(sorted(menu))] += 1

        count_menu = Counter(menu_dict).most_common()

        if count_menu:
            max = count_menu[0][1]

            for menu_pick, menu_num in count_menu:
                if menu_num >= 2 and menu_num == max:
                    result.append(''.join(menu_pick))

    return sorted(result)


# 수정한 풀이...
from collections import defaultdict
from itertools import combinations

def retNum(dicts, strings):
    len_course = len(strings)
    
    dic = defaultdict(int)
    for s in strings:
        for i in dicts[s]:
            dic[i] += 1
    
    cnt = 0
    for val in dic.values():
        if val == len_course:
            cnt += 1
    return cnt
        
def solution(orders, course):
    answer = []
    
    dicts = defaultdict(list)
    for idx, order in enumerate(orders,start=1):
        for o in order:
            dicts[o].append(idx)
    
    for c in course:
        cnt = 2
        for o in orders:
            # 콤비네이션 경우의 수를 줄이기 위해 order에 있는 알파벳만으로 경우의 수를 측정하였다.
            combis = list(combinations(o, c))
            for com in combis:
                tmp = retNum(dicts, com)
                com = ''.join(com)
                if tmp > cnt :
                    cnt = tmp
                    dicts[c] = [''.join(sorted(com))]
                elif tmp == cnt:
                    dicts[c].append(''.join(sorted(com)))
        if dicts[c]:
            answer.extend(dicts[c])
 
    answer = sorted(list(set(answer)))
    return answer


# 시간 초과된 코드...
from collections import defaultdict
from itertools import combinations

def retNum(dicts, strings):
    len_course = len(strings)
    
    dic = defaultdict(int)
    for s in strings:
        for i in dicts[s]:
            dic[i] += 1
    
    cnt = 0
    for val in dic.values():
        if val == len_course:
            cnt += 1
    return cnt
        
def solution(orders, course):
    answer = []
    menus = set()
    
    dicts = defaultdict(list)
    for idx, order in enumerate(orders,start=1):
        for o in order:
            menus.add(o)
            dicts[o].append(idx)
    
    for c in course:
        combis = list(combinations(menus, c))
        cnt = 2
        for com in combis:
            tmp = retNum(dicts, com)
            com = ''.join(com)
            if tmp > cnt :
                cnt = tmp
                dicts[c] = [''.join(sorted(com))]
            elif tmp == cnt:
                dicts[c].append(''.join(sorted(com)))
        if dicts[c]:
            answer.extend(dicts[c])

    return sorted(answer)