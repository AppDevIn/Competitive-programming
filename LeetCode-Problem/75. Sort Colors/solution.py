class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        RED, WHITE, BLUE = 0, 1, 2
        
        d = {RED: 0, WHITE: 0, BLUE: 0}
        
        for x in nums:
            d[x] = d[x]+1
        
        for index in range(len(nums)):
            
            if d[RED] > 0: nums[index] = RED
            elif d[WHITE] > 0: nums[index] = WHITE
            elif d[BLUE] > 0: nums[index] = BLUE
                
            d[nums[index]] = d[nums[index]] - 1
                
