class Solution:
    def decodeString(self, s: str) -> str:
        ans = []
                
        for i in range(len(s)):
            ans.append(s[i])
            
            if ans[-1] == ']':
                ans.pop()
                
                substr = ''
                numstr = ''
                while ans and ans[-1].isalpha():
                    substr = ans.pop() + substr
                
                ans.pop()
                while ans and ans[-1].isnumeric():
                    numstr = ans.pop() + numstr
                
                ans += (substr * int(numstr))
                    
        return ''.join(ans)