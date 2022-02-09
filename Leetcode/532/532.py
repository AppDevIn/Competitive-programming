import pdb


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        hashset = {}
        count = 0
        l = []
        for i in range(len(nums)):
            value = nums[i]
            temp = nums.pop(i)

            if (value-k) in nums:
                nums.insert(i, temp)
                hasValue = hashset.get(nums[i] + nums[i] - k, False)
                if hasValue: continue
                hashset[nums[i]+nums[i]-k] = True
                hashset[nums[i]-k, nums[i]] = True
                count += 1
            else:
                nums.insert(i, temp)

        return count


