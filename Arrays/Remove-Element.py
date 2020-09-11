class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        
        for x in range(nums.count(val)):
            nums.remove(val)
        return len(nums)
