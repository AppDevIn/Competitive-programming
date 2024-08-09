class Solution:
    def _isMagicSquare(self, grid, row, col):
        seen = [0]*9
        data = [0] * 5
        for r in range(row - 2, row + 1):
            colValue = 0
            index = 0
            for c in range(col - 2, col + 1):
                if grid[r][c] < 1 or grid[r][c] >= 10:
                    return False
                if seen[grid[r][c]-1] == 1:
                    return False
                seen[grid[r][c]-1] = 1
                colValue += grid[r][c]
                data[index] += grid[r][c]
                index += 1
            data.append(colValue)

        data[3] = grid[row - 2][col - 2] + grid[row - 1][col - 1] + grid[row][col]
        data[4] = grid[row - 2][col] + grid[row - 1][col - 1] + grid[row][col - 2]

        return len(set(data)) == 1

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        row = len(grid)
        col = len(grid[0])
        count = 0
        for r in range(2, row):
            for c in range(2, col):
                if self._isMagicSquare(grid, r, c):
                    count += 1
        return count

