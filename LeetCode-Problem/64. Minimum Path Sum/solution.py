class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rowSize = len(grid)
        colSize = len(grid[0])
        for row in range(rowSize):
            for col in range(colSize):
                if row == 0 and col == 0:
                    continue
                elif row == 0: 
                    grid[row][col] += grid[row][col-1]
                    continue
                elif col == 0: 
                    grid[row][col] += grid[row-1][col]
                    continue
                

                if grid[row][col-1] > grid[row-1][col]: grid[row][col] += grid[row-1][col]
                else: grid[row][col] += grid[row][col-1]
        return grid[rowSize-1][colSize-1]

