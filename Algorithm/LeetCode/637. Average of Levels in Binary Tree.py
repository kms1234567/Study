# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from collections import defaultdict
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        lev_dict = defaultdict(list)

        q = deque([[root, 0]])
        while q:
            node, lev = q.popleft()
            if node == None:
                continue
            lev_dict[lev].append(node.val)
            q.append([node.left, lev+1])
            q.append([node.right, lev+1])

        ans = []
        for l in sorted(list(lev_dict.keys())):
            ans.append(sum(lev_dict[l])/len(lev_dict[l])) 

        return ans


