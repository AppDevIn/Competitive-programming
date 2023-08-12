class Solution:
    def maxArea(self, height: List[int]) -> int:

        left, right = 0, len(height) - 1
        value = 0
        
        while left < right:
            newValue = min([height[left], height[right]]) * (right - left)
            if newValue > value:
                value = newValue

            if height[left] <= height[right]:
                left += 1
            else: right -= 1

        return value
