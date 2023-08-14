class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        l = []


        for i in range(len(nums)):
            if i > 0 and nums[i]==nums[i-1]: continue

            j, k = i + 1, len(nums) - 1

            while j < k:
                s = nums[i]+nums[j]+nums[k]

                if s > 0:k -= 1
                elif s < 0: j += 1
                else:
                    l.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j]==nums[j-1] and j < k: j+=1
        return l

        



