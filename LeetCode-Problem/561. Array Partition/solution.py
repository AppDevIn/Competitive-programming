class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        s, e = 0, 1
        res = 0
        while e < len(nums):
            res += min(nums[s], nums[e])
            s, e = e+1, e+2
        return res

            


        
