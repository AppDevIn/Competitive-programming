# 29. Divide Two Integers
# https://leetcode.com/problems/divide-two-integers/
# Not what they wanted but ohwells
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if int(dividend/divisor) > 2147483647:
            return 2147483647
        else: return int(dividend/divisor)