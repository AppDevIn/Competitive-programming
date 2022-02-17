# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/
import copy


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        l = []
        for x in candidates:
            l += self.df(target, [x], candidates, {})
        arr = []
        for x in l:
            x.sort()
            if x not in arr:
                arr.append(x)
        arr.sort()
        return arr

    def df(self, target, curr_list, candidates, hashSet):
        target = target - curr_list[-1]
        l = []
        if target == 0:
            l.append(curr_list)
            return l
        elif target > 0:
            filtered_list = filter(lambda x: x <= target, candidates)
            for x in filtered_list:
                temp = copy.deepcopy(curr_list)
                temp.append(x)
                l += self.df(target, temp, candidates, hashSet)
        else:
            return []

        return l


s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))
