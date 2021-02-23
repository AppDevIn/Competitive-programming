
# Version 01
# def searchMatrix(matrix, target):
#     """
#     :type matrix: List[List[int]]
#     :type target: int
#     :rtype: bool
#     """
    
#     for m in matrix:
#         if target in m:
#             return True
#     return False
    
# Version 02
# def searchMatrix(matrix, target):
#     """
#     :type matrix: List[List[int]]
#     :type target: int
#     :rtype: bool
#     """

#     newMatrix = []
#     for x in matrix:
#         if x[0] <= target:
#             newMatrix.append(x)
#     matrix = newMatrix
#     newMatrix = []
    
#     if matrix == []: return False
#     row = 0
#     col = len(matrix[0]) - 1

#     while(col >= 0 and col < len(matrix[0]) and row >= 0 and row < len(matrix)):
#         if (target == matrix[row][col]):
#             return True
#         elif target > matrix[row][col]:
#             row += 1
#         elif target < matrix[row][col]:
#             col -= 1
#     return False

# Version 03
# def searchMatrix(matrix, target):
#     """
#     :type matrix: List[List[int]]
#     :type target: int
#     :rtype: bool
#     """
    
#     row = 0
#     col = len(matrix[0]) - 1

#     while(col >= 0 and col < len(matrix[0]) and row >= 0 and row < len(matrix)):
#         if (target == matrix[row][col]):
#             return True
#         elif target > matrix[row][col]:
#             row += 1
#         elif target < matrix[row][col]:
#             col -= 1
#     return False


#Version 04
def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """


    
    row = 0
    col = len(matrix[0]) - 1

    while(col >= 0 and col < len(matrix[0]) and row >= 0 and row < len(matrix)):
        if (target == matrix[row][col]):
            return True
        elif target > matrix[row][col]:
            row += 1
        elif target < matrix[row][col]:
            col -= 1
    return False


searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20)