class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        row, col = 0, 0
        RIGHT, DOWN, LEFT, UP = 1, 2, 3, 4
        PATH = RIGHT
        res = []
        total_nums = len(matrix) * len(matrix[0])
        mid = total_nums // 2 + 1 

        while len(res) + 1 != total_nums:
            if PATH == RIGHT:
                while (col + 1) < len(matrix[row]) and matrix[row][col+1] != "x":
                    res.append(matrix[row][col])
                    matrix[row][col] = "x"
                    col += 1
                PATH = DOWN
            elif PATH == DOWN:
                while (row + 1)< len(matrix) and matrix[row+1][col] != "x" :
                    res.append(matrix[row][col])
                    matrix[row][col] = "x"
                    row += 1
                PATH = LEFT
            elif PATH == LEFT:
                while  col-1 >= 0 and matrix[row][col-1] != "x" :
                    res.append(matrix[row][col])
                    matrix[row][col] = "x"
                    col -= 1
                PATH = UP
            elif PATH == UP:
                while row-1 >= 0 and matrix[row-1][col] != "x":
                    res.append(matrix[row][col])
                    matrix[row][col] = "x"
                    row -= 1
                PATH = RIGHT
        return res + [matrix[row][col]]
