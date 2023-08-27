class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        oneP, twoP = len(num1) - 1, len(num2) - 1
        remainder = 0
        res = 0
        temp = ""
        while twoP >= 0:

            s = int(num1[oneP]) * int(num2[twoP]) + remainder
            
            remainder = 0
            
            if s >= 10 and oneP != 0:
                temp = str(s % 10) + temp
                remainder = s // 10
            else:
                temp = str(s) + temp
            
            
            if oneP == 0 and twoP >= 0:
                
                res += int(temp) 
                twoP -= 1
                oneP = len(num1) 
                temp = "0"*(len(num2) - 1 -twoP)
            oneP -= 1
        return str(res)


            
        
