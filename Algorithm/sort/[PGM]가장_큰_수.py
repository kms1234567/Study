from functools import cmp_to_key
def numeric_compare(x, y):
    tmp1 = x + y
    tmp2 = y + x
    return (int(tmp1) > int(tmp2)) - (int(tmp1) < int(tmp2))

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = cmp_to_key(numeric_compare), reverse=True)
    return str(int(''.join(numbers)))