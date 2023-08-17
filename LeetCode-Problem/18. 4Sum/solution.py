class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = set()
        for a, n in enumerate(nums):
            
            for b in range(a+1,len(nums)):
                c,d = b + 1, len(nums) - 1
                while c < d:
                    s = n + nums[b] + nums[c] + nums[d] 

                    if s < target:
                        c += 1
                    elif s > target:
                        d -= 1
                    elif s == target:
                        ans.add((n, nums[b], nums[c], nums[d]))
                        c += 1
                        d -= 1
        return ans


