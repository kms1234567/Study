# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def solution(node, arr) -> list:
            if node.left == None and node.right == None:
                arr.append(node.val)
            
            if node.left != None:
                solution(node.left, arr)
            if node.right != None:
                solution(node.right, arr)
            return arr
        return solution(root1, []) == solution(root2, [])
