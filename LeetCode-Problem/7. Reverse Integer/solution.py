class Solution:
    def reverse(self, x: int) -> int:
        neg = x < 0
        x = abs(x)
        start = 10 ** (len(str(x)) - 1)
        val = 0
        ex = 1
        
        while start >= 1:
            val += (x // start) * ex
            x = x % start
            ex *= 10
            start /= 10
        val = (int(val) if not neg else -int(val))

        if val >= 0 and val <= 2**31-1: return val
        if val < 0 and val >= -2**31: return val
        return 0
            
