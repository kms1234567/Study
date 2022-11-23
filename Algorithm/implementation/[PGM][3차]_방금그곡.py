# https://school.programmers.co.kr/learn/courses/30/lessons/17683

# 깔끔 풀이

def shap_to_lower(s):
    s = s.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    return s

def solution(m,musicinfos):
    answer=[0,'(None)']   # time_len, title
    m = shap_to_lower(m)
    for info in musicinfos:
        split_info = info.split(',')
        time_length = (int(split_info[1][:2])-int(split_info[0][:2]))*60+int(split_info[1][-2:])-int(split_info[0][-2:])
        title = split_info[2]
        part_notes = shap_to_lower(split_info[-1])
        full_notes = part_notes*(time_length//len(part_notes))+part_notes[:time_length%len(part_notes)]
        if m in full_notes and time_length>answer[0]:
            answer=[time_length,title]
    return answer[-1]

# 내 풀이

dicts = {'C':'a', 'C#':'b', 'D':'c', 'D#':'d', 'E':'e', 'F':'f', 'F#':'g', 'G':'h', 'G#':'i', 'A':'j', 'A#':'k', 'B':'l', 'E#':'m'}
def changeString(string):
    
    ret_str = []
    len_str = len(string)
    string += '0'
    
    for i in range(len_str):
        if string[i] == '#':
            continue
        
        if string[i+1] == '#':
            ret_str.append(dicts[string[i] + string[i+1]])
        else:
            ret_str.append(dicts[string[i]])
            
    return ''.join(ret_str)            
    
def retTime(start, end):
    start_hour, start_minuet = start.split(':')
    end_hour, end_minuet = end.split(':')
    
    end_time = int(end_hour) * 60 + int(end_minuet)
    start_time = int(start_hour) * 60 + int(start_minuet)

    total = end_time - start_time
 
    return total
    
def solution(m, musicinfos):
    answer = '(None)'
    max_time = 0
    
    melody = changeString(m)

    for info in musicinfos:
        datas = info.split(',')
        start = datas[0];end = datas[1]
        total = retTime(start, end)
        
        ans = datas[2]
        music = changeString(datas[3])
        len_music = len(music)

        music = music + (music*((total//len_music)))

        if melody in music[:total]:
            if max_time < total:
                answer = ans
                max_time = total

    return answer