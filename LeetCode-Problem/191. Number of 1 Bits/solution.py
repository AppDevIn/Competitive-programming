class Solution:
    def hammingWeight(self, n: int) -> int:
        maxBit = 2147483648
        
        count = 0
        while n > 0:
            if n >= maxBit:
                count += 1
                n -= maxBit
            maxBit /= 2
            
            

        return count
