# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        # 그 위에 서브트리들의 조건까지도 막족해야하는데, 고려하지 않았음
        # -inf < target < inf 의 조건을 시작으로 left와 right를 범위를 갱신해나가면서 비교해야함.
        
        INF = 2**31+1
        
        def dfs(left, right, node):
            ans = True
            if node == None:
                return True
            if left >= node.val or node.val >= right:
                return False
        
            ans = dfs(left, node.val, node.left) & dfs(node.val, right, node.right)
            
            return ans
        
        return dfs(-INF, INF, root)