# https://leetcode.com/problems/longest-palindromic-substring/





# 내가 푼 코드 시간초과
import re
# 토마토 스위스 기러기 별똥별 우영우 같은 문자들을 'Palindromic Substring' 이라고 한다.
class Solution(object):
    def longestPalindrome(self, s):
        # 중복 문자 사이의 글자가 두 글자면 합격. ex) aa, bb, cc
        # a b c d c b a     1 2 3 4 5 6 7    중복되는 문자들이 옆에 글자와 같이 대칭을 이뤄야함
        # a b b a
        # 비교하는 횟수를 줄이기 위해 현재 max len을 구한 후,
        # 비교하려는 길이가 max len보다 작으면 넘어간다.
        
        result = ''
        max_len = 0
        char = set()
        for c in s:
            # 중복 방지
            if c in char:
                continue
            char.add(c)
            
            p = re.compile(c)
            res = p.finditer(s)
            
            span_list = []
            for r in res:
                span_list.append(r.span())
            span_len = len(span_list)
            
            for i in range(0, span_len-1):
                for j in range(i+1, span_len):
                    first = span_list[i]
                    last = span_list[j]
                    
                    # tmp_str의 길이
                    tmp_len = last[1] - first[0]
                    if (tmp_len <= max_len):
                        continue
                    
                    # tmp_epoch는 대칭횟수를 몇 번 탐색할 것인지
                    tmp_epoch = tmp_len // 2
                    # tmp_str은 비교하려는 str이다.
                    tmp_str = s[first[0] : last[1]]
                    
                    isSubString = True
                    for k in range(0, tmp_epoch):
                        if(tmp_str[k] != tmp_str[-1-k]):
                            isSubString = False
                            
                    if (isSubString):
                        max_len = max(max_len, tmp_len)  
                        result = tmp_str
                        
        if result:
            return result
        else:
            return s[0]
        """
        :type s: str
        :rtype: str
        """ 