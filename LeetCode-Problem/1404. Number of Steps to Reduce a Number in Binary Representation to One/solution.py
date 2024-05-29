class Solution:
    def numSteps(self, s: str) -> int:
        decimal_number = int(s, 2)
        
        count = 0
        while decimal_number != 1:
        
            if decimal_number % 2 == 0:
                decimal_number //= 2
            else:
                decimal_number += 1
            count += 1
        return count

        
