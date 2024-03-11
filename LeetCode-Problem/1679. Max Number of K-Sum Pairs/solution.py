class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        p1, p2 = 0, len(nums)-1

        nums.sort()
        res = 0
        while p1 < p2: 
            if nums[p1] + nums[p2] == k:
                p1 += 1
                p2 -= 1
                res += 1
            elif nums[p1] + nums[p2] > k:
                p2 -= 1
            elif nums[p1] + nums[p2] < k:
                p1 += 1
        return res




        
