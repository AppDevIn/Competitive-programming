class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        self.checked = []
        def df(left, up, right, down):
            if left > right or up > down:
                return False
            elif target < matrix[up][left] or target > matrix[down][right]:
                return False

            mid = (left + right) // 2

            row = up 
            while row <= down and matrix[row][mid] <= target:
                if target == matrix[row][mid]: return True
                row += 1

            return df(left, row, mid-1, down) or df(mid+1, up, right, row-1)

        return df(0, 0, len(matrix[0])-1, len(matrix)-1 )
