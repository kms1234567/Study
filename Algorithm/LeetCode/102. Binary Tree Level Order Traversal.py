# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        def bfs():
            q = deque()
            if root != None:
                q.append([1, root])
            
            while q:
                lev, node = q.popleft()
                if len(ans) < lev:
                    ans.append([node.val])
                else:
                    ans[lev-1].append(node.val)
                
                if node.left != None:
                    q.append([lev+1, node.left])
                if node.right != None:
                    q.append([lev+1, node.right])    
            
        bfs()
        return ans