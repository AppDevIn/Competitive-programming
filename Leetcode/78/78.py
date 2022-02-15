# 78. Subsets
# https://leetcode.com/problems/subsets/

import copy


class Solution:
    def subsets(self, nums):
        lst = []

        for i, x in enumerate(nums):
            arr = []
            arr.append([x])
            if i is not 0:

                for j in lst:
                    j = copy.deepcopy(j)
                    j.append(x)
                    arr.append(j)

            lst+=arr
        lst.insert(0, [])
        return lst


s = Solution()
print(s.subsets([1, 2, 3]))
