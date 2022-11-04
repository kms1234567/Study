def solution(S):
    dicts = {']':'[', '}':'{', ')':'('}
    comment_dicts = {'*/':'/*'}
    close_comments = comment_dicts.keys()
    
    closes = dicts.keys()
    S = list(S)
    stk = []

    while S:
        bracket = S.pop()
        if bracket in closes:
            stk.append(bracket)
        else:
            if not stk:
                return 'FALSE'
            else:
                if dicts[stk[-1]] != bracket:
                    return 'FALSE'
                else:
                    stk.pop()
    return 'TRUE' if not stk else 'FALSE'

print(solution("(/*()}[*/)"))