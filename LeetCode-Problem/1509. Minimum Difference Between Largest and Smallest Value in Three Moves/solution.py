class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        nums.sort()
 
        min_diff = float("inf")
        for i in range(4):
            right = len(nums) - 4 + i
            min_diff = min(min_diff, nums[right] - nums[i])
        return min_diff
   

        
