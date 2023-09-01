class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for row in range(n):
            for x in range(n-1,-1,-1):
                val = matrix[x].pop(0)
                matrix[row].append(val)
                
