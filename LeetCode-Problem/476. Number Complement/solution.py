class Solution:
    def findComplement(self, num: int) -> int:

        bit = 1
        while bit < num: bit *= 2

        complement = 0
        noLeadingZero = False
        while bit >= 1:
            if num >= bit:
                noLeadingZero = True
                num -= bit
            elif noLeadingZero:
                complement += bit
            
            bit /= 2
        return int(complement)
