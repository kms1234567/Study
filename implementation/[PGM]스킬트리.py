# https://school.programmers.co.kr/learn/courses/30/lessons/49993

# 깔끔한 풀이
def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer


from collections import defaultdict
def checkSkill(s, skill, dicts):
    if s not in skill:
        return True
    
    s_idx = skill.index(s)
    if not s_idx:
        dicts[s] = True
    else:
        if dicts[skill[s_idx-1]]:
            dicts[s]=True
        else:
            return False
    return True

def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        dicts = defaultdict(bool)
        isCorrect = True
        for s in skills:
            if not checkSkill(s, skill, dicts):
                isCorrect = False
                break
        
        if isCorrect:
            answer += 1
  
    return answer