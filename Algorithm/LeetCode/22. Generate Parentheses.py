# 깔끔 풀이
class Solution:  
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def recursion(opened:int, closed:int, n:int, tmp:str):
            if len(tmp) == 2*n:
                ans.append(tmp)
                return
            # 열린괄호는 어느 경우에서든 n 보다 작으면 넣어도 된다.
            if opened < n:
                recursion(opened+1, closed, n, tmp + '(')
            # 닫힌 괄호는 항상 열린괄호보다 개수가 적은 상태에서 기입해야 한다.
            if closed < opened: 
                recursion(opened, closed+1, n, tmp + ')')
                
        recursion(0, 0, n,'')
        return ans


class Solution:
    def check(self, n: int, tmp:str):
        stk = []
        tmp = list(tmp)
        
        while tmp:
            p = tmp.pop()
            if p == '(':
                if not stk:
                    return False
                else:
                    stk.pop()
            elif p == ')':
                stk.append(')')
        if stk:
            return False
        
        return True
    
    def recursions(self, n: int, tmp: str, ans: list):
        if len(tmp) == n*2:
            if self.check(n, tmp):
                ans.append(tmp)
            return
        
        self.recursions(n, tmp+'(', ans)
        self.recursions(n, tmp+')', ans)
        
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.recursions(n, '', ans)
        return ans

    
   