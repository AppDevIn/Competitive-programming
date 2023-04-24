class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        curr = nums[0]
        arr = nums
        for x in arr[1::]:
            if x > curr:
                curr = x
            else: 
                nums.remove(x)
        nums = arr
        return len(arr)
