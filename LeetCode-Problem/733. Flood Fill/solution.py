
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        
        queue = [(sr, sc)]
        changed = set()
        rowSize, colSize = len(image)-1, len(image[0])-1
        pathNum = image[sr][sc]

        while queue:
            row, col = queue.pop(0)
            
            rowChange = min(row+1, rowSize)
            if image[rowChange][col] == pathNum and (rowChange, col) not in changed:
                queue.append((rowChange, col))
            rowChange = max(row-1, 0)
            if image[rowChange][col] == pathNum and (rowChange, col) not in changed:
                queue.append((rowChange, col))
            colChange = min(col+1, colSize)
            if image[row][colChange] == pathNum and (row, colChange) not in changed:
                queue.append((row, colChange))
            colChange = max(col-1, 0)
            if image[row][colChange] == pathNum and (row, colChange) not in changed:
                queue.append((row, colChange))
            image[row][col] = color
            changed.add((row, col))
        return image

