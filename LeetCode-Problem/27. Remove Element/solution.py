class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size = len(nums)
        index = 0
        while index < size:
            if nums[index] == val:
                del nums[index]
                size -= 1
            else:
                index += 1
        
        return size

