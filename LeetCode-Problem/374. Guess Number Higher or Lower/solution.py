# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        guessValue = guess(n)
        if guessValue == 0:
            return n
        mi, mx = 1, n 
        while guessValue != 0:
            guessValue = guess(mi + ((mx - mi)//2))
            if guessValue == 1:
                mi = mi + ((mx - mi)//2)
            elif guessValue == -1:
                mx = mi + ((mx - mi)//2)
            
        return mi + ((mx - mi)//2)
