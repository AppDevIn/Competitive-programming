class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        
        for count in range(len(nums)-1):
            if nums[count] == nums[count+1]:
                return True

        return False
