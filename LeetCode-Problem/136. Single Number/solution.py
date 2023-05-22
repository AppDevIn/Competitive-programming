class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        index = 0
        while len(nums) > 1:
            val = nums[index]
            del nums[index]
            if val in nums:
                nums.remove(val)
            else:
                return val
        return nums[0]
            
