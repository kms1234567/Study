class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dynamic programming

        # 모든 인덱스에서의 숫자는 최소 1개의 최대길이를 가질 수 있기 때문에 모두 1로 초기화한다.
        # 그리고 마지막 숫자부터 순차적으로 처음까지 이동을 하며, 값을 갱신한다.
        # 1. 만약 현재 숫자가 다음 숫자보다 크다면 continue를 통해 무시한다.
        # 2. 만약 현재 숫자가 다음 숫자보다 작다면, 현재 내 최대 길이와 해당 길이에 + 1을 한 값중 최대를 저장한다.
        # 3. 이를 반복한다.
        # 4. 이렇게 풀 경우 n^2으로 해결할 수 있다.

        LIS = [1] * len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(i, len(nums)):
                if nums[i] >= nums[j]:
                    continue
                LIS[i] = max(LIS[j] + 1, LIS[i])

        return max(LIS)



from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        bisect를 이용한 풀이. bisect_left는 정렬된 배열에서 해당 숫자가 어느 인덱스에 들어갈지 알려주는 함수이다.
        만약 현재 숫자가 스택 마지막 숫자보다 크다면 그대로 append를 진행한다.
        만약 현재 숫자가 스택 마지막 숫자보다 작다면 해당 숫자를 어느 인덱스에 넣을지 판단 후, 변경한다.
        이를 반복한다.
        이렇게 풀 경우 bisect_left는 O(logn)의 시간이 걸리므로
        n번 반복할 경우, 최대 O(nlogn)의 시간이 걸려 n^2보다 높은 성능을 보인다.
        """
        stk = []
        
        for num in nums:
            if not stk or stk[-1] < num:
                stk.append(num)
            else:
                idx = bisect_left(stk, num)
                stk[idx] = num
        return len(stk)