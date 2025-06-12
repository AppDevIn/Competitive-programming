class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        start, end = 0, 1
        maximum = float('-inf')
        while end < len(nums):
            maximum = max(maximum, abs(nums[start] - nums[end]))
            start = end
            end = end + 1
        
        maximum = max(maximum, abs(nums[0] - nums[len(nums) - 1]))

        return maximum


        
