class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:

        directions = [(0,1), (1, 0), (0, -1), (-1, 0)]
        cleaned = []
        visited = []
        row, col = 0, 0
        directionIndex = 0
        maxRow, maxCol = len(room), len(room[0])

        while (row, col, directionIndex) not in visited:
            if col in [-1, maxCol] or row in [-1, maxRow] or room[row][col] == 1:
                visited.append((row, col, directionIndex))
                row -= directions[directionIndex][0]
                col -= directions[directionIndex][1]
                directionIndex = (directionIndex + 1) % 4
                r, c = directions[directionIndex]
                row += r
                col += c
            else:
                if (row, col) not in cleaned:
                    cleaned.append((row, col))
                r, c = directions[directionIndex]
                row += r
                col += c
        
        return len(cleaned)
    
                




        
        
