# https://leetcode.com/problems/longest-substring-without-repeating-characters/
from collections import defaultdict

# 솔루션 -> 완전 탐색
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def check(start, end):
            chars = set()
            for i in range(start, end + 1):
                c = s[i]
                if c in chars:
                    return False
                chars.add(c)
            return True

        n = len(s)

        res = 0
        for i in range(n):
            for j in range(i, n):
                if check(i, j):
                    res = max(res, j - i + 1)
        return res


# 내가 푼 답
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
        # dict_list에는 해당 문자가 몇번째인지가 들어간다
        dict_list = defaultdict(int)
        max_cnt = 0;cnt = 0
        # max_cnt는 답을 가리키고, cnt는 계속해서 1씩 증가하지만 중간에 중복된 문자가 나오면 바뀔 수도 있다.
        for idx, tmp in enumerate(s, start=1):
            cnt += 1
            
            # 만약 이미 있는 문자라면
            # 현재 cnt와 중복된 문자사이의 거리를 비교해서 작은 값을 cnt로 지정한다.
            if (dict_list[tmp] != 0):
                cnt = min(cnt, idx - dict_list[tmp])
                
            dict_list[tmp] = idx
            max_cnt = max(max_cnt, cnt)
        
        return max_cnt
        
        """               
        :type s: str
        :rtype: int
        """