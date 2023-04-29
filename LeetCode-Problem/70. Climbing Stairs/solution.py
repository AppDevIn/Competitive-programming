class Solution:
    def climbStairs(self, n: int) -> int:
        t, prev, curr = 0, 0, 1
        for i in range(n):
            t =  prev  + curr
            prev = curr
            curr = t
        return t
