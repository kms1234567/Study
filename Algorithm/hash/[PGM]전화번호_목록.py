# https://school.programmers.co.kr/learn/courses/30/lessons/42577

# 정석 풀이
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer

# 내 풀이
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        len1 = len(phone_book[i]);len2 = len(phone_book[i+1])
        
        if len1 >= len2:
            continue
        elif phone_book[i] == phone_book[i+1][:len1]:
            return False
    
    return True

# 22.10.20
def solution(phone_book):
    phone_book.sort()
    for i in range(1, len(phone_book)):
        if phone_book[i-1] == phone_book[i][:len(phone_book[i-1])]:
            return False
    return True