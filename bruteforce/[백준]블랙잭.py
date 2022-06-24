def solution(depth, idx, tmp_cards):
    if depth == 3:
        val_sum = sum(tmp_cards)
        if val_sum <= M:
            res_cards.append(val_sum)
        return
    
    for i, val in enumerate(cards):
        if i > idx:
            tmp_cards.append(val)
            solution(depth+1, i, tmp_cards)
            tmp_cards.pop() 

N, M = map(int, input().split())
cards = list(map(int, input().split()))

cards.sort(reverse = True)

res_cards = []

solution(0, -1, [])

print(max(res_cards))