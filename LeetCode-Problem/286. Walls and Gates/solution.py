class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROW, COL = len(rooms), len(rooms[0])
        visit = set()
        queue = []
        
        def addRoom(r, c):
            if (r < 0 or r == ROW or c < 0 or c == COL or (r, c) in visit or rooms [r][c] == -1):
                return 
            visit.add((r, c)) 
            queue.append([r, c])
    
        for row in range(ROW):
            for col in range(COL):
                if rooms[row][col] == 0:
                    visit.add((row, col))
                    queue.append([row, col])
        dist = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.pop(0)
                rooms[r][c] = dist
                addRoom(r+ 1, c) 
                addRoom (r - 1, c) 
                addRoom(r, c + 1)
                addRoom(r, c- 1)
            dist += 1
            
                
                
    
                    
                    
                    
                    
                    
