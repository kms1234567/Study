# https://school.programmers.co.kr/learn/courses/30/lessons/64064

from itertools import permutations
import re

def solution(user_id, banned_id):
    answer = set()

    banned = (' '.join(banned_id).replace('*', '.'))
    
    # user_id 로 만들 수 있는 모든 경우의 수를 먼저 만들어 놓음.
    for permu in list(permutations(user_id, len(banned_id))):
        if re.match('^'+banned+'$', ' '.join(permu)):
            answer.add(''.join(sorted(permu)))  

    return len(answer)