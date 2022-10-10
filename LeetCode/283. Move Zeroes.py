class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 시간초과 하나하나씩 비교해가면서 한칸씩 모두 옮기느 방법으로 brute-force 형식
        # f = 0
        # e = len(nums)-1       
        # while f < e:
        #     num = nums[f]
        #     if not num:
        #         front = f
        #         while front < e:
        #             nums[front], nums[front + 1] = nums[front + 1], nums[front]
        #             front +=1
        #         e -= 1                
        #     if nums[f]:
        #         f += 1
        
        # 숫자가 있는 경우에 해당 숫자를 front 위치와 변경한다. 0일 경우에는 front가 올라가지 않으므로, front는 계속 맨 앞 0의 위치를 가리키게 된다.
        front = 0
        for idx, num in enumerate(nums):
            if num:
                nums[front], nums[idx] = nums[idx], nums[front]
                front += 1