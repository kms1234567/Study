# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        ans = ''
        
        if x < 0:
            x = str(x)
            ans += '-'
            ans += x[-1:0:-1]
        else:
            x = str(x)
            ans += x[-1::-1]
        
        ans = int(ans)
        if ans < -2**31 or ans > 2**31-1:
            return 0
        
        return int(ans)