class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p0 = 0
        p2 = len(nums)-1
        
        cur = 0
        
        # 0일 경우 p0 인덱스의 값과 위치를 바꾼 후, cur을 1 증가
        # 2일 경우 p2 인덱스의 값과 위치를 바꾼 후, cur은 증가시키지 않음. 해당 숫자가 또 2일 수도 있기 때문이다.
        # 1일 경우에는 cur만 증가시킨다.해당 인덱스가 0의 마지막위치 일수도 있기 때문이다. 만약, 후에도 0이 나온다면 해당 1의값과 바꾸기 때문에 상관없다.
        while cur <= p2:
            
            if nums[cur] == 0:
                nums[cur], nums[p0] = nums[p0], nums[cur]
                cur += 1
                p0 += 1
            elif nums[cur] == 2:
                nums[cur], nums[p2] = nums[p2], nums[cur]
                p2 -= 1
            else:
                cur += 1
