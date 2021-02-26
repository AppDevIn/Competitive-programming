# 581. Shortest Unsorted Continuous Subarray
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/solution/
class Solution(object):

    def findUnsortedSubarray(self, nums: [int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """

        last = len(nums) - 1
        index = 0

        left = len(nums)
        right = 0

        for first in range(len(nums)):
            for i in range(max(right, first), len(nums)):
                if nums[first] > nums[i]:
                    right = max(i,right) 
                    left = min(first, left)

        
        return 0 if right - left <= 0 else (right - left) + 1
            
            


solution = Solution()

print(solution.findUnsortedSubarray([1,2,3,4]))