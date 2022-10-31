class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stk1 = []
        stk2 = []
        
        for i in range(len(s)):
            if s[i] != '#':
                stk1.append(s[i])
                continue
            elif stk1:
                stk1.pop()
                
        for i in range(len(t)):
            if t[i] != '#':
                stk2.append(t[i])
                continue
            elif stk2:
                stk2.pop()
                
        return True if ''.join(stk1) == ''.join(stk2) else False