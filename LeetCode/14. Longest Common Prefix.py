class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        
        # 배열안에 있는 값을 하나씩 빼낸다. 길이가 다를 경우 제일 작은 값까지만 가져오게 됨.
        for s in zip(*strs):
            # 가져온 튜플을 set화 해서 길이가 1이면 모두 같은 글자를 가진 것이므로 추가한다.
            if len(set(s)) == 1:
                ans += s[0]
            else:
                break
                
        return ans