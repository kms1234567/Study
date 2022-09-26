# https://leetcode.com/problems/longest-palindromic-substring/

class Solution(object):
    def longestPalindrome(self, s):
        
        answer = s[0];len_answer = 1
        len_s = len(s)
        # 2가지 로 나눠서 
        
        for i in range(len_s-1):
            j = 1
            while i-j >= 0 and i+j < len_s and s[i-j] == s[i+j]:
                if 2*j + 1 > len_answer:
                    len_answer = 2*j + 1
                    answer = s[i-j:i+j+1]
                j += 1
                
            j = 0
            while i-j >= 0 and i+j+1 < len_s and s[i-j] == s[i+j+1]:
                if 2 + 2*j  > len_answer:
                    len_answer = 2 + 2*j 
                    answer = s[i-j:i+j+2]
                j += 1
        return answer
                
        
        """
        :type s: str
        :rtype: str
        """
        