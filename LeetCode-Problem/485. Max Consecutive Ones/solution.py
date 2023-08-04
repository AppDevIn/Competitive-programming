class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        maxCount, count = 0, 0
        for b in nums:
            if b == 1:
                count += 1
            else:
                count = 0
            
            if count > maxCount:
                maxCount = count
        return maxCount
