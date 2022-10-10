# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
하위 오른쪽 서브트리와 왼쪽 서브트리의 위치를 모두 변경시킨다.
모든 트리에 순회하면서 left 서브트리와 right 서브트리의 위치를 변경시킨다.
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if node == None:
                return
            
            dfs(node.left)
            dfs(node.right)
            node.left, node.right = node.right, node.left            
            
        dfs(root)
        return root