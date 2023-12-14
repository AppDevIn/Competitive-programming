class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def calculate(index, sum, t):
            if index == len(nums):                    
                    return 1 if sum == t else 0
            if (index, sum) in dp:
                return dp[(index, sum)]
            dp[(index, sum)] = calculate(index + 1, sum + nums[index], t) + calculate(index + 1, sum - nums[index], t)
            return dp[(index, sum)]
        
        return calculate(0, 0, target)
        
