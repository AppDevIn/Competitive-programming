class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: return "0"
        if num < 0: num = (2**32) + num

        hexa = "0123456789abcdef"
        ans = ""
        while num > 0:
            ans = hexa[num%16] + ans 
            num //= 16 
        return ans
