# 560. Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/
import pdb


class BruteSolution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        value = 0
        for i in range(len(nums)):
            l = [nums[i]]
            if sum(l) == k:
                value += 1

            for s in nums[i + 1:]:
                l.append(s)
                if sum(l) == k:
                    value += 1
                print(l)
        return value


s = BruteSolution()

print(s.subarraySum([0, 0], 0))

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        hashSet = {0: 1}
        result = 0
        l = []
        for n in nums:
            l.append(n)
            t = sum(l)
            s = t - k
            result += hashSet.get(s, 0)
            hashSet[t] = hashSet.get(t, 0) + 1

        return result


s = Solution()

print(s.subarraySum([1, 1, 1], 2))
