class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def check(s:str) -> bool:
            set_list = set(s)
            for char in set_list:
                if char.islower():
                    if char.upper() not in set_list:
                        return False
                elif char.isupper():
                    if char.lower() not in set_list:
                        return False
            return True
        
        ans = ''
        front = 0
        while front < len(s):
            for end in range(front+1, len(s)):
                if check(s[front:end+1]):
                    if end+1-front > len(ans):
                        ans = s[front:end+1]
            front += 1
        return ans