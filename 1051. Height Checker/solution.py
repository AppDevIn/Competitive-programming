
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = copy.deepcopy(heights)
        swapped = True
        while swapped:
            swapped = False
            index = 0
            counter = 0
            while index + 1 < len(heights):
                if heights[index] != expected[index]:
                    counter += 1
                if heights[index] > heights[index+1]:
                    temp = heights[index]
                    heights[index] = heights[index + 1]
                    heights[index + 1] = temp
                    swapped = True
                index += 1
        if heights[-1] != expected[-1]:
            counter += 1
        return counter
                
            
        
