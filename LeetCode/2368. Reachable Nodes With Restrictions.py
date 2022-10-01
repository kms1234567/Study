from collections import defaultdict
class Solution(object):
    def reachableNodes(self, n, edges, restricted):
        """
        :type n: int
        :type edges: List[List[int]]
        :type restricted: List[int]
        :rtype: int
        """
        graph = defaultdict(list)
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False for _ in range(n)]
        restricts = [False for _ in range(n)]
        
        for r in restricted:
            restricts[r] = True
        
        def dfs(node=0):
            visited[node] = True
            
            for new_node in graph[node]:
                if not visited[new_node] and not restricts[new_node]:
                    dfs(new_node)
        dfs()           
        return sum(visited)