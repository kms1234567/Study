# https://school.programmers.co.kr/learn/courses/30/lessons/17678

def timeToNum(time):
    h, m = time.split(':')
    return int(h)*60 + int(m)

def numToTime(time):
    h = str(time//60)
    m = str(time%60)
    
    return h.zfill(2)+':'+m.zfill(2)
    
def solution(n, t, m, timetable):
    timetable_len = len(timetable)
    
    for i in range(timetable_len):
        timetable[i] = timeToNum(timetable[i])
    
    bustable = []
    bustable.append(timeToNum('09:00'))
    for _ in range(n-1):
        bustable.append(bustable[-1] + t)

    # 1. timetable의 개수가 m보다 적거나 같으면 가장 늦은 시간대가 정답
    if timetable_len < m :
        return numToTime(bustable[-1])
    
    # 2. timetable의 개수가 많으면 차례대로 소거해가면서 마지막 시간대에서 남은 시간대 중 탈 수 있는 가장 늦은 시간대를 선정한다.
    timetable.sort(reverse = True)
    stk = [];cnt = 0
    for bus in bustable:
        cnt = 0
        while timetable and timetable[-1] <= bus and cnt < m:
            cnt += 1
            stk.append(timetable.pop())
        continue
    
    # 만약 마지막 버스에 탑승한 사람이 m보다 작으면 가장 늦은 시간대에 탑승 가능
    if cnt < m:
        return numToTime(bustable[-1])
    # 그렇지 않고, m보다 크거나 같으면 가장 마지막에 탑승한 승객보다 1분 먼저 도착하면 된다.
    else:
        return numToTime(stk[-1]-1)