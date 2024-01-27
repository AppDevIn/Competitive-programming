class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for curr in range(len(nums)):
            smallest = curr
            for index in range(curr,len(nums)):
                if nums[smallest] > nums[index]:
                    smallest = index
            temp = nums[curr]
            nums[curr] = nums[smallest]
            nums[smallest] = temp
                
                
