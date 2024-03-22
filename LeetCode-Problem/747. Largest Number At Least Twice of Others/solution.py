class Solution:
    def dominantIndex(self, nums: List[int]) -> int:


        m, p = 0, 0
        mi, pi = -1, -1
        for i,x in enumerate(nums):

            if x > m:
                p,m = m, x
                pi,mi = mi, i
            elif x > p:
                p, pi = x, i

        return mi  if m >= p*2 else -1
