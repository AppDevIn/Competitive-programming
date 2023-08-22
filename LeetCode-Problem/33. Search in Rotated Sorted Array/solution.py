class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1
        res = -1
        while l < r:
            if target == nums[r]:
                res = r
            elif target == nums[l]:
                res = l
            l += 1
            r -= 1
        return res


