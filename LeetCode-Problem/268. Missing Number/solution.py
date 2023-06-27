class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
        leftValue, rightValue = 1, n 
        nums.sort()

        if n == 1:
            return 0 if nums[0] == 1 else 1
        while right - left >= -1:
            if nums[left] == 0:
                left += 1
            elif nums[right] == 0:
                right -= 1
            if leftValue != nums[left]:
                return leftValue
            elif rightValue != nums[right]:
                return rightValue
            
            left += 1 
            right -= 1
            leftValue += 1
            rightValue -= 1
        return 0
