class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1. 맨 끝에서부터 보면서 증가하다가 숫자가 하강하는 지점의 인덱스를 찾는다.
        # 2. 해당 인덱스 전 숫자(바꿔야할 숫자)보다 바로 직후로 큰 숫자 하나를 끝 인덱스부터 찾는다.
        # 3. 해당 숫자와 변경 후, 바뀐 숫자 밑에 있는 내림차순되어있는 숫자들을 오름차순으로 정렬해준다.
        
        i = j = r = len(nums) - 1
        
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1
        
        if not i:
            nums.reverse()
            return
        
        k = i - 1
        for l in range(j, k, -1):
            if nums[k] < nums[l]:
                nums[k], nums[l] = nums[l], nums[k]
                break
                
        l = k+1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1;r -= 1