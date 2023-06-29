class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        counter = 0
        zero = 0
        while counter < len(nums) - zero:
            if nums[counter] == 0:
                nums.append(nums[counter])
                del nums[counter]
                zero += 1
            else: counter += 1
            
        

            

