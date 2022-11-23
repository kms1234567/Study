S = input()
T = input()

# S->T로 변환하는 것이 아니라 T->S 로 변환
def dfs(input):
    ans = False
    if ''.join(input) == S:
        return True
    elif len(input) <= len(S):
        return False

    if input[-1] == 'A':
        input.pop()
        ans = ans or dfs(input)
        input.append('A')
    if input[0] == 'B':
        ans = ans or dfs((input[1:])[-1::-1])
    return ans

print(1 if dfs(list(T)) else 0)