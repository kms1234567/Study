from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Counter를 이용하여 개수를 센 후, 1개인 넘버를 리턴하였다.
        counter = Counter(nums)
        
        for key in counter.keys():
            if counter[key] == 1:
                return key

        # 사기정답 차례대로 not 연산을 사용해서 나온 답이 정답이다.
        return reduce(lambda x, y : x ^ y, nums)