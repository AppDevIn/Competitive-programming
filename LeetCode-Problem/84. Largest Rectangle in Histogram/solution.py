class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        def right(pos, height, heights, count=0):
            if pos >= len(heights): return count
            if heights[pos] >= height:
                return right(pos+1, height, heights, count+1)
            return count

            
        
        def left(pos, height, heights, count=0):
            if pos < 0: return count
            if heights[pos] >= height:
                return left(pos-1, height, heights, count+1)
            return count

        area = 0
        m = max(heights)*len(heights)
        for index, height in enumerate(heights):

            area = max(area, left(index-1, height, heights)*height + height + right(index+1, height, heights)*height)
            if area >= m: return area
            
        return area

