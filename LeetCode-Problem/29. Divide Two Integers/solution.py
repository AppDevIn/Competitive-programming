class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        count = len(range(0, abs(dividend)-abs(divisor)+1, abs(divisor)))
        
        count = count if (divisor >= 0 and dividend >= 0) or (divisor < 0 and dividend < 0) else -count

        return count if -(2**31) <= count < (2**31 - 1) else (2**31 - 1)




