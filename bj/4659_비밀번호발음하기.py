vowels = {'a', 'e', 'i', 'o', 'u'}
def solution(str):
    is_vowel = False
    cnt_vowel, cnt_consonant = 0, 0
    prev_char = ''

    for char in str:
        if char in vowels:
            is_vowel = True
            cnt_vowel += 1
            cnt_consonant = 0
        else:
            cnt_consonant += 1
            cnt_vowel = 0
        
        if cnt_vowel >= 3 or cnt_consonant >= 3:
            return False

        if prev_char == char and char != 'e' and char != 'o':
            return False

        prev_char = char

    if not is_vowel:
        return False
    else:
        return True
    
while True:
    id = input()
    if id == 'end':
        break
    is_check = solution(id)
    sentence = '<{0}> '.format(id)
    if is_check:
        sentence += 'is acceptable.'
    else:
        sentence += 'is not acceptable.'
    print(sentence)
