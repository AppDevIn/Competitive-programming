class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        n = len(nums)
        nums = set(nums)
        missing = []
        left, right = 1, n
        while left < right:
            if right not in nums:
                missing.append(right)
            if left not in nums:
                missing.append(left)
            right -= 1
            left += 1  
            
            
        return missing

