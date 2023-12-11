from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def depth(visited, row, col):
            stack = [(row, col)]
            while stack:
                current_row, current_col = stack.pop()

                if (
                    0 <= current_row < ROW
                    and 0 <= current_col < COL
                    and (current_row, current_col) not in visited
                    and grid[current_row][current_col] == "1"
                ):
                    visited.add((current_row, current_col))
                    stack.append((current_row + 1, current_col))
                    stack.append((current_row, current_col + 1))
                    stack.append((current_row - 1, current_col))
                    stack.append((current_row, current_col - 1))


        visited = set()
        ROW, COL = len(grid), len(grid[0])
        res = 0

        for row in range(ROW):
            for col in range(COL):
                if (row, col) not in visited and grid[row][col] == "1":
                    res += 1
                    depth(visited, row, col)

        return res

