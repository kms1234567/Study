from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        ans = []
        # deque 을 이용하여 레벨순회하여 오른쪽만 ans에 넣어서 풀이
        def bfs(node, level):
            q = deque()
            q.append([node, level])
            
            while q:
                n, l = q.popleft()
                v = n.val
                if len(ans) < l:
                    ans.append(v)
                else:
                    ans[l-1] = v
                
                if n.left != None:
                    q.append([n.left, l+1])
                if n.right != None:
                    q.append([n.right, l+1])
        
        bfs(root, 1)
        return ans