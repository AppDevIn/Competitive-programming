class Solution:
    def canJump(self, nums: List[int]) -> bool:
        total = 0
        farthest = 0
        for index in range(len(nums)):
            farthest = max(farthest, index+nums[index])
            if farthest >= len(nums) -1:
                return True
            elif nums[index] == 0 and farthest <= index: return False
            
            
        return False

