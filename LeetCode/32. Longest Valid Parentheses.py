class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 답에서 인덱스를 같이 넣어준다.
        # 답에서 오름차순으로 정렬 후, 연속되는 올바른 괄호 개수를 센다.
      
        ans = []
        closed = 0
        
        closed_stk = []
        s = list(s)
        for i, p in enumerate(s[-1::-1]):
            if p == ')':
                closed += 1
                closed_stk.append(i)
            else:
                if closed:
                    closed -= 1
                    j = closed_stk.pop()
                    ans.append(i)
                    ans.append(j)
        ans.sort()
        answer = 0
        cnt = 0
        if ans:
            prev = ans[0]-1
        for num in ans:
            if num == prev + 1:
                cnt += 1
            else:
                answer = max(answer,cnt)
                cnt = 1
            prev = num
        answer = max(answer, cnt)   
        
                    
        return answer
        