class Solution:
    def _flooFill(self, grid, row, col):
        if row < 0 or row > len(grid)-1:
            return 
        elif col < 0 or col > len(grid)-1:
            return 
        elif grid[row][col] == 1 or grid[row][col] == 2:
            return
        grid[row][col] = 2
        self._flooFill(grid, row + 1, col)
        self._flooFill(grid, row - 1, col)
        self._flooFill(grid, row, col + 1)
        self._flooFill(grid, row, col - 1)

    def regionsBySlashes(self, grid: List[str]) -> int:
        grid_size = len(grid)
        regions = 0
        expanded_grid = [[0] * (grid_size * 3) for _ in range(grid_size * 3)]
        for i in range(grid_size):
            for j in range(grid_size):
                base_row = i * 3
                base_col = j * 3

                if grid[i][j] == "\\":
                    expanded_grid[base_row][base_col] = 1
                    expanded_grid[base_row + 1][base_col + 1] = 1
                    expanded_grid[base_row + 2][base_col + 2] = 1
                elif grid[i][j] == "/":
                    expanded_grid[base_row][base_col + 2] = 1
                    expanded_grid[base_row + 1][base_col + 1] = 1
                    expanded_grid[base_row + 2][base_col] = 1

        for r in range(len(expanded_grid)):
            while 0 in expanded_grid[r]:
                self._flooFill(expanded_grid, r, expanded_grid[r].index(0))
                regions += 1

        print(expanded_grid)
        return regions

