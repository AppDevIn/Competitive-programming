# 645. Set Mismatch
# https://leetcode.com/problems/set-mismatch/
class Solution:
    def findErrorNums(self, nums):
        
        length = len(nums)

        ori = [z for z in range(1, length+1)]
        num = [n for n in nums]

        for x in nums:
            if x in ori:
                num.remove(x)
                ori.remove(x)
        num.extend(ori)
        return num
                
        

s = Solution()
s.findErrorNums(nums=[1,2,2,4])