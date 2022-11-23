# https://school.programmers.co.kr/learn/courses/30/lessons/67256

dicts = {1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2],
        '*':[3,0], 0:[3,1], '#':[3,2]}
left_coordinate = dicts['*']
right_coordinate = dicts['#']

def hand_check(hand, num):
    target = dicts[num]
    right_val = abs(right_coordinate[0] - target[0]) + abs(right_coordinate[1] - target[1]) 
    left_val = abs(left_coordinate[0] - target[0]) + abs(left_coordinate[1] - target[1]) 

    if right_val > left_val:
        ret = 'left'
    elif right_val < left_val:
        ret = 'right'
    else:
        if hand == 'right':
            ret = 'right'
        else:
            ret = 'left'
    return ret
    
def solution(numbers, hand):
    global left_coordinate;global right_coordinate
    answer = ""
    
    left_nums = [1, 4, 7]
    right_nums = [3, 6, 9]
    
    for num in numbers:
        if num in left_nums:
            answer += 'L'
            left_coordinate = dicts[num]
        elif num in right_nums:
            answer += 'R'
            right_coordinate = dicts[num]
        else:
            h = hand_check(hand, num)
            if h == 'right':
                answer += 'R'
                right_coordinate = dicts[num]
            else:
                answer += 'L'
                left_coordinate = dicts[num]
        
    return answer