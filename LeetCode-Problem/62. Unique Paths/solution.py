## Unique Paths

### Problem Description

A robot is located at the top-left corner of a grid `(m, n)`. The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid. How many unique paths are there?

### Solution

We can solve this problem using dynamic programming. We'll create a 2D array to store the number of unique paths to each cell. We'll initialize all cells in the first row and the first column to `1` because there is only one way to reach these cells (by moving either down or right).

Then, we'll iterate through the grid starting from the second row and the second column. For each cell, we'll calculate the number of unique paths to it by summing the number of paths from the cell above it and the cell to the left of it.

Finally, the value in the bottom-right cell of the 2D array will represent the number of unique paths from the top-left corner to the bottom-right corner of the grid, which is our answer.

### Python Code

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D array to store the number of unique paths to each cell
        dp = [[1] * n for _ in range(m)]

        # Calculate the number of unique paths for each cell
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]

