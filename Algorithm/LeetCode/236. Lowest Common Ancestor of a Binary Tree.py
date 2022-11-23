from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
레벨 순회를 하면서 해당 p와 q노드의 경로를 저장합니다.

이후, p와 q노드중 겹치는 경로까지 진행을 하면 해당 노드가 LCS(가장 가까운 조상노드)가 됩니다.
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_dir = q_dir = ''
        
        nodes = []
        
        def bfs():
            nonlocal p_dir
            nonlocal q_dir
            queue = deque()
            queue.append([root, ''])
            while queue:
                node, path = queue.popleft()
                if node == None:
                    nodes.append(None)
                    continue
                else:
                    nodes.append(node)
                if node.val == p.val:
                    p_dir = path
                if node.val == q.val:
                    q_dir = path                
                queue.append([node.left, path+'l'])
                queue.append([node.right, path+'r'])
        
        bfs()
        
        path = ''
        for k, l in zip(p_dir, q_dir):
            if k == l:
                path += k
            else:
                break

        for c in path:
            if c == 'l':
                root = root.left
            elif c == 'r':
                root = root.right 
                
        return root