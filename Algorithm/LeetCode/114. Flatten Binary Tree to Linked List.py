






# 첫 풀이
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        dummy = TreeNode(None)
        dummy = deepcopy(root)
         # root -> left -> right
         # 가리키는 더미 복사본을 만들어서 재귀로 전달
        
        def traversal(dummy):
            nonlocal root
            if dummy == None:
                return 

            if dummy.left != None:
                left_val = dummy.left.val
                root.left = None
                root.right = TreeNode(left_val)
                root = root.right
                traversal(dummy.left)

            if dummy.right != None:
                right_val = dummy.right.val
                root.left = None
                root.right = TreeNode(right_val)
                root = root.right
                traversal(dummy.right)
        traversal(dummy)