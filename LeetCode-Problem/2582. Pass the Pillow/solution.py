class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        n -= 1
        IS_ODD = (time // n) % 2 == 1
        remainder = (time % n)
        n += 1
        if IS_ODD:
            return n - remainder 
        return remainder + 1


        
