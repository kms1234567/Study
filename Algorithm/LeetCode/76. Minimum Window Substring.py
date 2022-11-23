"""

처음에는 보석쇼핑 문제처럼 하면되는 줄 알았으나, s에 t의 문자열이 모두 포함되는 것이 아니었다.
t에는 중복문자까지 나오므로 개수까지 알아봐야 했다.
그래서 처음에 t 문자들의 개수를 세고, t의 key값을 need 변수에 저장한다.
내가 해당 t에 있는 unique한 문자에 개수까지 만족할 때마다 have의 개수를 1씩 올린다. 이 때, 이미 올려진 애들은 다시 -1을 해줘야 한다.
그렇게 해서 have와 need가 같아질 때, left에 있는 포인터를 1씩 올리면서 해당 만족이 깨질 때까지 올리면서 answer을 갱신한다.
만약 have의 개수가 1줄어들게 되었다면, 다시 for문을 진행하여 have의 개수가 만족할 때까지 right 개수를 올린다.
have의 개수가 다시 만족하게 되었다면 while문을 들어가 left를 올리면서 answer 갱신을 반복한다.

"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ''
        t_counter = defaultdict(int)
        for c in str(t):
            t_counter[c] += 1
        t = set(t)
    
        s_counter = defaultdict(int)
        have = 0
        
        # unique한 t의 개수와 hava의 개수가 같아야 한다. 물론 중복되는 데이터가 t에 있을 수 있으므로
        # have의 값을 올릴 때는 해당 캐릭터의 개수가 목표 캐릭터의 개수보다 많은지 확인 후 올려야 한다.
        left = 0
        for right in range(len(s)):
            if s[right] in t:
                # 이미 충족되는 상황이었으면 -1을 한다. 어짜피 올릴 것이다.
                if s_counter[s[right]] >= t_counter[s[right]]:
                    have -= 1
                s_counter[s[right]] += 1
                # 개수가 충족되면 have의 개수를 높인다.
                if s_counter[s[right]] >= t_counter[s[right]]:
                    have += 1
                    
            while have == len(t_counter):
                if not ans:
                    ans = s[left:right+1]
                elif len(ans)> right+1-left:
                    ans = s[left:right+1]
                
                if s[left] in t:
                    s_counter[s[left]] -= 1
                    if s_counter[s[left]] < t_counter[s[left]]:
                        have -= 1
                left += 1
                
        return ans    