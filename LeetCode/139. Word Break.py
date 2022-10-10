class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # dynamic programming
        # 끝 글자 인덱스를 True로 설정한다.
        # 끝 글자(i)에서부터 내려가면서 word의 길이(w)만큼 더해서 일치할 경우 dp[i] = dp[i+w] 로 기록한다.
        
        dp = [False] * (len(s) +1)
        dp[len(s)] = True
        
        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if (i + len(word) <= len(s) and s[i:i+len(word)] == word):
                    dp[i] = dp[i+len(word)]
                if dp[i]:
                    break
        return dp[0]