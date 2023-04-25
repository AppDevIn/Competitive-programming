class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        start = 0
        end = len(nums)

        while end - start != 1:
            if target < nums[start:end][(end-start)//2]:
                end = (start+end) // 2 
            else:
                start = (start+end) // 2
            
        return start if target <= nums[start] else end
