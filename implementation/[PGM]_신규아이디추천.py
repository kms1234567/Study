# https://school.programmers.co.kr/learn/courses/30/lessons/72410

import re
def solution(new_id): 
    # 1. 대문자->소문자
    new_id = new_id.lower()
    
    # 2. 소문자 숫자 - _ . 을 제외한 모든 문자 제거
    new_id = re.sub('[^ a-z0-9-_.]', '', new_id)
    
    # 3. . 이 2번 이상 연속된 부분을 하나의 .으로 변경한다.
    new_id = re.sub('[.]+' , '.', new_id)
    
    # 4. .이 처음이거나 끝에 위치한다면 제거한다.
    new_id = new_id.strip(".")
    
    # 5. 빈 문자열이라면 new_id에 a를 대입한다.
    if not new_id :
        new_id = 'a'
    
    # 6. 아이디의 길이가 16자 이상이라면 첫 15개의 문자를 제외한 모든 문자 제거. 제거 후 마침표가 new_id의 끝에 위치한다면 끝 마침표를 제거한다.
    if len(new_id) >= 16:
        new_id = new_id[0:15]
  
    while new_id and new_id[-1] =='.':
        new_id = re.sub('[.]$' , '', new_id)
    
    # 7. 아이디의 길이가 2자 이하라면 아이디의 마지막 문자를 길이가 3이 될 때 까지 반복해서 끝에 붙인다.
    while len(new_id) < 3:
        new_id += new_id[-1]
    return new_id