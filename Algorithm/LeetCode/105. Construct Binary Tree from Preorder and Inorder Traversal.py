# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



"""
preorder와 inorder를 보고 트리를 만드는 문제이다.
preorder 특성상 첫 번째 원소는 항상 루트노드임을 보장하며, inorder 특성상 특정 노드의 왼쪽은 모두 왼쪽 서브트리 오른쪽은 오른쪽 서브트리임을 보장한다.
이를 이용하여 recursive 하게 풀어야 한다.
"""
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        # recursive 재귀 풀이
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left  = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root