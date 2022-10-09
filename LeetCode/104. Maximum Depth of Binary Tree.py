# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def bfs():
            ans = 0
            q = deque()
            if root != None:
                q.append([1, root])
            while q:
                lev, node = q.popleft()
                ans = max(ans,lev)
                if node.left != None:
                    q.append([lev+1, node.left])
                if node.right != None:
                    q.append([lev+1, node.right])
            return ans
        
        return bfs()