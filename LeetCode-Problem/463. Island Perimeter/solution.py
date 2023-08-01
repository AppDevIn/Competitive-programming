class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        row, plot = 0, 0
        parimeter = 0
        while row < len(grid):
            if plot >= len(grid[row]):
                row += 1
                plot = 0
                continue
            
            if grid[row][plot] == 0:
                plot += 1
                continue
            
            if (plot != 0 and grid[row][plot-1] == 0) or plot == 0:
                parimeter += 1
            if (plot + 1 < len(grid[row]) and grid[row][plot+1] == 0) or plot >= len(grid[row])-1:
                parimeter += 1
            if (row != 0 and grid[row-1][plot] == 0) or row == 0:
                parimeter += 1
            if (row + 1 < len(grid) and grid[row+1][plot] == 0) or row >= len(grid) - 1:
                parimeter += 1
            plot += 1
        return parimeter
        
            


