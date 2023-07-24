class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        maxVal = nums[0]
        m = maxVal
        index, count = 1, 1
        while index < len(nums) and count != 3:
            if nums[index] != m:
                count += 1
                m = nums[index]
            
            index += 1
        return m if count == 3 else maxVal

            

