class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        res = 0
        
        def addToQueue(queue, row, col):
            if row >= ROW or col >= COL:
                return 
            if row < 0 or col < 0:
                return 
            if grid[row][col] == "1" and (row, col) not in visited:
                queue.append([row, col])
                visited.add((row, col))
            elif grid[row][col] == "0" and (row, col) not in visited:
                visited.add((row, col))
            
        
        for row in range(ROW):
            for col in range(COL):
                if (row, col) in visited: continue
                if grid[row][col] == "0": continue
                res += 1

                q = [[row, col]]
                visited.add((row, col))
                
                while q:
                    r, c = q.pop(0)
                    addToQueue(q, r + 1, c)
                    addToQueue(q, r - 1, c)
                    addToQueue(q, r, c + 1)
                    addToQueue(q, r, c - 1)
                    
        return res
