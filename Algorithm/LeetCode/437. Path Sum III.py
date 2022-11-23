# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# bruteforce
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root, val):
            if root == None:
                return 0
            res = 0
            if root.val == val: res += 1
            res += dfs(root.left, val-root.val)
            res += dfs(root.right, val-root.val)
            return res
                
        if root == None: 
            return 0
        return self.pathSum(root.left, targetSum) + dfs(root, targetSum) + self.pathSum(root.right, targetSum)

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count: List[int] = [0]
        lookup: Dict[int, int] = {0: 1}
        
        def preorder(node: Optional[TreeNode], prev_sum: int) -> None:
            if not node:
                return
              
            curr_sum: int = prev_sum + node.val
            x: int = curr_sum - targetSum
            
            if x in lookup:
                count[0] += lookup[x]
            
            lookup[curr_sum] = lookup.get(curr_sum, 0) + 1
            
            preorder(node.left, curr_sum)
            preorder(node.right, curr_sum)
            
            lookup[curr_sum] -= 1
        
        preorder(root, 0)
        
        return count[0]