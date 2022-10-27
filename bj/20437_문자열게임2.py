from collections import deque
T = int(input())

for _ in range(T):
    game = input()
    num = int(input())
    alphas = set()

    min_ans, max_ans = 10**9, 1
    for front in range(len(game)):
        target = game[front]
        if target in alphas:
            continue

        alphas.add(target)
        q = deque([front])
        end = front + 1
        
        while end < len(game):
            if game[front] == game[end]:
                q.append(end)
            if len(q) == num:
                tmp = q[-1] - q[0] + 1
                min_ans = min(min_ans, tmp)
                max_ans = max(max_ans, tmp)
                q.popleft()
            end += 1
        
    if max_ans < num:
        print(-1)
    else:
        if num == 1:
            min_ans = 1
        print(min_ans, max_ans)