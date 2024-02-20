class Solution:
    def climbStairs(self, n: int) -> int:
        def helper(steps, des, mem):
            if steps in mem: return mem[steps]
            if steps > des: return 0
            if steps==des: return 1
            if steps <des: 
                N = helper(steps+1, n, mem) + helper(steps+2, n, mem)
                mem[steps] = N
                return N
        return helper(0, n, {})
    
    
