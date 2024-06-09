class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        if n > k:
            return k 

        kR = k - (n-1)
        remainder = kR % (n-1)
        multipler = int(kR / (n-1))

        if multipler % 2 == 0:
            return n - 1 - remainder
        else:
            return remainder 


