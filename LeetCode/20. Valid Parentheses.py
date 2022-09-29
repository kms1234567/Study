class Solution:
    def isValid(self, s: str) -> bool:
        # 스택 이용하는 방법
        s = list(s)
        stack = []
        
        parenthes = {'(' : ')', '[':']', '{':'}'}
        
        keys = parenthes.keys()
        
        while s:
            par = s.pop()
            
            if par in keys:
                if not stack:
                    return False
                else:
                    if parenthes[par] != stack.pop():
                        return False
            else:
                stack.append(par)
        if stack:
            return False
        return True