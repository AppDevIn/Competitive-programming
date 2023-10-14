class Solution:
    def findMin(self, nums: List[int]) -> int:
        print(nums)
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return nums[0] if nums[0] < nums[1] else nums[1]

        mid = (len(nums)-1)//2
        print(mid)
        if nums[mid] > nums[len(nums)-1]:
            return self.findMin(nums[mid+1::])
        else:
            return self.findMin(nums[0:mid+1])


