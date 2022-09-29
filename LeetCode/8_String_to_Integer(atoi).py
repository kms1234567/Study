import re
class Solution:
    def myAtoi(self, s: str) -> int:
        # 1. 공백을 없애줌
        s = s.strip()
        # 2. 문자열이 비었으면 0리턴
        if not s:
            return 0
        # 3. 앞 글자가 +, -, 혹은 아무것도 없는 경우에 match를 시킨다.
        # match의 경우에는 앞글자부터 확인한다. search는 모든 경우를 찾아보기에 알맞지 않음.
        if s[0] == '+':
            match_num = re.match('[+]\d+', s)
        elif s[0] == '-':
            match_num = re.match('[-]\d+', s)
        else:
            match_num = re.match('\d+', s)
        
        # 4. 없으면 0리턴, 있으면, 숫자로 변환
        if not match_num:
            return 0
        if match_num:
            ans = int(match_num[0])
        
        if ans > 2**31 -1:
            ans = 2**31 - 1
        elif ans < -2**31:
            ans = -2**31
            
        return ans