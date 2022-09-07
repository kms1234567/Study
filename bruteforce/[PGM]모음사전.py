# https://school.programmers.co.kr/learn/courses/30/lessons/84512

from itertools import product
def solution(word):
    # 중복순열이 가능한 것 product
    alpha_list = ['A', 'E', 'I', 'O', 'U']
    
    product_list = []
    for i in range(1, 6):
        for com in list(product(alpha_list, repeat = i)):
            product_list.append(''.join(com))
    product_list.sort()
    
    return product_list.index(word)+1