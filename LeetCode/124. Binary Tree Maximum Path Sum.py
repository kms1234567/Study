# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 결국은 순간순간에 왼쪽 서브트리합과 오른쪽 서브트리합 중 무엇을 선택할 것인지의 연속.
        # 리프 도느는 왼쪽,오른쪽이 0을반환 하므로 자기 자신
        # 만약 더하고 있는 값이 음수이면 0으로 치환해서 더해줌. <- 가지않겠다
        # 각각의 값들은 ans에 갱신시켜가면서 진행.
        ans = [root.val]
        def dfs(node):
            if node == None:
                return 0
            
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            
            ans[0] = max(ans[0], leftMax + rightMax + node.val)
            
            return node.val + max(leftMax, rightMax)
        dfs(root)
        return ans[0]