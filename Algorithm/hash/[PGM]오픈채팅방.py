# https://school.programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    dicts_info = dict()
    dicts_id = dict()
    
    for idx, info in enumerate(record):
        data = info.split(' ')
        com = data[0];uid = data[1]
        if com != 'Leave':
            nic = data[2]
        if com == 'Enter':
            dicts_info[idx] = [uid,'님이 들어왔습니다.']
            dicts_id[uid] = nic            
        elif com == 'Leave':
            dicts_info[idx] = [uid,'님이 나갔습니다.']
        else:
            dicts_id[uid] = nic
        
    return [dicts_id[nic]+info for nic, info in dicts_info.values()]