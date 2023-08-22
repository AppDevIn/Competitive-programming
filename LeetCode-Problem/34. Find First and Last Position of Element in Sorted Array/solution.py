class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 1 and nums[0] == target: return [0, 0]

        l, r = 0, len(nums) - 1
        start = -1
        while l <= r:

            mid = (l + r) // 2

            if nums[mid] == target:
                start = mid
                break

            if target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        if start == -1:
            return [-1, -1]
        
        
        end = start
        while (start-1 >= 0 and nums[start] == nums[start-1]) or (end +1 < len(nums) and nums[end] == nums[end+1]):
            if end +1 < len(nums) and nums[end] == nums[end + 1]:
                end += 1        
            if start - 1 >= 0  and nums[start] == nums[start - 1]:
                start -= 1
        return [start, end]

