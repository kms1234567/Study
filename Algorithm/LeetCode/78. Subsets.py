from itertools import product

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        arrs = []
        # nums에 있는 숫자들과 공백을 각각 넣고 product를 통해 해결하였다.
        for num in nums:
            arrs.append([[], [num]])
        
        product_list = list(product(*arrs))
        
        for p in product_list:
            ans.append(sum(p, []))
            
        return ans