class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 해당 인덱스에 대한 목표(마지막 인덱스)를 줄여나가면서
        # 최종적으로 첫 번째 인덱스가 목표가 될 때까지 간다.
        goal = len(nums) - 1
        
        for i in range(len(nums)-1, -1, -1):
            # 현재 인덱스 + 점프거리가 goal 보다 크거나 같으면 현재 목표를 해당 인덱스로 변경한다.
            if i + nums[i] >= goal:
                goal = i
       
        return True if not goal else False
       