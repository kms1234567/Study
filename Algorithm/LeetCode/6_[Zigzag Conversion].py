from collections import deque
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans = []
        q = deque(s)
        
        # 같은 행에있는 애들끼리 인덱스를 저장해놓은 다음, 
        # 인덱스를 기준으로 sort하여 출력한다.
        while q:
            cnt = 0
            while q and cnt != numRows-1:
                ans.append([cnt, q.popleft()])
                cnt += 1
                
            while q and cnt != 0:
                ans.append([cnt, q.popleft()])
                cnt -= 1
        
        ans.sort(key = lambda x : x[0])
        
        return ''.join([s[1] for s in ans])