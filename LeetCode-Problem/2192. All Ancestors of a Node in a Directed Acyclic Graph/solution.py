
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = {i: [] for i in range(n)}
        for frm, to in edges:
            graph[to].append(frm)
        
        ancestors = [set() for _ in range(n)]
        curr = 0
        def dfs(node: int, visited: Set[int]):
            for parent in graph[node]:
                if parent not in visited:
                    visited.add(parent)
                    ancestors[curr].add(parent)
                    dfs(parent, visited)
        
        for i in range(n):
            curr = i
            dfs(i, set())

        return [sorted(list(ancestors[i])) for i in range(n)]
        
