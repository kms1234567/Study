class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 풀이 1
        # 복사본을 만들고 rotate될 위치에 복사본의 원래 값을 넣는다.
        original = nums.copy()
        
        for i in range(len(nums)):
            j = (i+k) % len(nums)
            nums[j] = original[i]
        
        
        # 비슷한 풀이. tmp-dicts에 복사본 값들을 저장하였다.
        tmp_dicts = dict()
        
        for idx, num in enumerate(nums):
            tmp_dicts[idx] = num
            
        for idx, num in enumerate(nums): 
            rotate_idx = (idx + k) % len(nums)
            nums[rotate_idx] = tmp_dicts[idx]
