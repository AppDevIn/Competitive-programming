# https://leetcode.com/problems/single-number/
# 136. Single Number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        arr = set(nums)
        for x in arr:
            nums.remove(x)
            if x not in nums:
                return x



s = Solution()
print(s.singleNumber([2,2,1]))