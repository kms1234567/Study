# 그리디
from collections import defaultdict
def make_timetable(a_time, b_time, c_time, d_time):
    counter = defaultdict(int)
    over = defaultdict(int)
    weeks = defaultdict(list)

    times = {'10':0, '11':1, '12':2, '13':3, '14':4, '15':5, '16':6, '17':7}
    days = {'Mon':0, 'Tue':1, 'Wed':2, 'Thu':3, 'Fri':4}
    ans = [['X' for _ in range(8)] for _ in range(5)]

    # a='Mon15' -> ans[days[a[:3]]][times[a[3:]]]
    for day, a_t, b_t, c_t, d_t in zip(days.keys(), a_time, b_time, c_time, d_time):
        a_t = a_t.split(';');b_t = b_t.split(';');c_t = c_t.split(';');d_t = d_t.split(';')
        for a in a_t:
            a = a.split('~')
            for time in range(int(a[0][:2]), int(a[1][:2])):
                weeks[day+str(time)].append('A')
                counter['A'] += 1
        for b in b_t:
            b = b.split('~')
            for time in range(int(b[0][:2]), int(b[1][:2])):
                weeks[day+str(time)].append('B')
                counter['B'] += 1

        for c in c_t:
            c = c.split('~')
            for time in range(int(c[0][:2]), int(c[1][:2])):
                weeks[day+str(time)].append('C')
                counter['C'] += 1

        for d in d_t:
            d = d.split('~')
            for time in range(int(d[0][:2]), int(d[1][:2])):
                weeks[day+str(time)].append('D')
                counter['D'] += 1

    for w in weeks.keys():
        d = days[w[:3]]
        t = times[w[3:]]
        if len(weeks[w]) == 1:
            if over[weeks[w][0]] >= 10:
                if ans[d][t] == 'X':
                    ans[d][t] = 'E'
                    continue

            ans[d][t] = weeks[w][0]
            over[weeks[w][0]] += 1
            counter[weeks[w][0]] -= 1
        elif len(weeks[w]) >= 2:
            min_name = weeks[w][0]
            for name in weeks[w]:
                if over[name] >= 10:
                    if ans[d][t] == 'X':
                        ans[d][t] = 'E'
                    continue
                if counter[name] < counter[min_name]:
                    min_name = name
                counter[name] -= 1

            ans[d][t] = min_name
            over[min_name] += 1

    print(ans)


make_timetable(['10:00~14:00', '15:00~18:00', '11:00~13:00;14:00~16:00', '10:00~11:00', '15:00~18:00'],
['11:00~14:00', '14:00~16:00', '16:00~18:00', '10:00~11:00;12:00~13:00', '14:00~16:00'],
['14:00~16:00', '16:00~18:00', '10:00~12:00', '12:00~14:00', '14:00~16:00'],
['14:00~18:00', '10:00~18:00', '12:00~14:00', '14:00~15:00;16:00~17:00', '10:00~12:00'])

# ['10:00~14:00', '15:00~18:00', '11:00~13:00;14:00~16:00', '10:00~11:00', '15:00~18:00']
# ['11:00~14:00', '14:00~16:00', '16:00~18:00', '10:00~11:00;12:00~13:00', '14:00~16:00']
# ['14:00~16:00', '16:00~18:00', '10:00~12:00', '12:00~14:00', '14:00~16:00']
# ['14:00~18:00', '10:00~18:00', '12:00~14:00', '14:00~15:00;16:00~17:00', '10:00~12:00']