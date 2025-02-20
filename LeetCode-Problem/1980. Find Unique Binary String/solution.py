class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums.sort()  
        num = 0  

        for n in nums:
            binary_representation = format(num, f'0{len(nums[0])}b')  
            if n != binary_representation:  
                return binary_representation
            num += 1  


        return format(num, f'0{len(nums[0])}b')

