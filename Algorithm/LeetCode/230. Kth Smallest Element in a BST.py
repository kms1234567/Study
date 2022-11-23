# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 가장 작은 것은 맨 왼쪽. 그 다음은 루트. 그 다음은 오른쪽 중에서도 왼쪽
        
        ans = []
        def dfs(node):
            if node == None:
                return
            
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)
        dfs(root)
        return ans[k-1]