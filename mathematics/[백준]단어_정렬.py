# https://www.acmicpc.net/problem/1181
N = int(input())

word_aligns = []

# 해당 단어의 개수와 단어를 리스트에 넣는다.
for _ in range(N):
    a = input()
    word_aligns.append((len(a), a))
# 중복되는 단어들을 지운다.
word_aligns = list(set(word_aligns))
# 먼저 개수로 오름차순 정렬 후, 단어 정렬을 후순위로 둔다.
word_aligns.sort(key=lambda x:(x[0],x[1]))

for i in word_aligns:
    print(i[1])