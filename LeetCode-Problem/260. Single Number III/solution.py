class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        nums.sort()
        i, j = 0, 1
        while j < len(nums):
            if nums[i] == nums[j]:
                nums.pop(j)
                nums.pop(i)
            else:
                i = j
                j += 1
        return nums
            


        
            


        
