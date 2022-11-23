# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def dfs(left, right):
            ans = True
            if left == None or right == None:
                if left != right:
                    return False
                else:
                    return True
            
            if left.val != right.val:
                return False
            
            ans = dfs(left.left, right.right) & dfs(left.right, right.left)
            
            return ans
            
        return dfs(root.left, root.right)    