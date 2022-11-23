class Solution(object):
    def isPali(self, s):
        len_s = len(s)
        
        start = 0
        end = len_s - 1
        
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
            
        return True
               
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # bruteforce + backtracking -> 모든 경우의 수를 찾는다.
        
        ans = []
        tmp = []
        
        def dfs(i):
            if i >= len(s):
                ans.append(tmp+[])
                return
            
            for j in range(i, len(s)):
                if self.isPali(s[i:j+1]):
                    tmp.append(s[i:j+1])
                    dfs(j+1)
                    tmp.pop()
        dfs(0)
        return ans