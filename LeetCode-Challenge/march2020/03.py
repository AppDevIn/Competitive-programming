# 268. Missing Number
# https://leetcode.com/problems/missing-number/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        for x in range(0, len(nums)+1):
            if x in nums:
                nums.remove(x)
            else:
                return x
                
        