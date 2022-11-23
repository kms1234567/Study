# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        curList = []
        def dfs(node):
            cnt = 0
            if node == None:
                return cnt
            
            curList.append(node.val)
            if max(curList) <= node.val:
                cnt += 1
            cnt += dfs(node.left)
            cnt += dfs(node.right)
            curList.pop()
            return cnt

        return dfs(root)
