import random
from collections import defaultdict

def mix_members(members):
    random.shuffle(members)

    answer = defaultdict(list)
    operand = 7
    share, remainder = divmod(len(members), operand)
    splits = [operand for _ in range(share)] + [remainder]

    while splits[-1] < 5:
        for i in range(len(splits)-1, -1, -1):
            if splits[-1] < 5:
                splits[i] -= 1
                splits[-1] += 1
            else: break
    
    stndr = 0
    for team, split in enumerate(splits, start = 1):
        team = str(team) + '조'
        answer[team] = members[stndr:stndr+split]
        stndr += split

    return answer

print(mix_members(['손보영', '이시혁', '강원재', '복문혁', '풍희훈', '정다혜', '류민정', '박경윤', '안은수', '하재현', '서원경', '탁승희', '고해남', '장종환', '사공범호', '유미옥', '탁예준', '문기훈', '사공우주', '남경희', '복으뜸', '조빛가람', '탁샘', '김샘', '정우람', '신미르', '노버들', '장한결', '탁힘찬', '백샘', '서나길', '남궁우람', '손미르', '백한길', '하한결', '양샘', '심나라우람', '장한길', '풍한결', '성다운']))