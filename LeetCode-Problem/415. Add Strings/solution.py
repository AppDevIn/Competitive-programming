class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        first, second = num2, num1
        if len(num1) > len(num2):
            first = num1
            second = num2
        
        count, index, remainder = 0, -1, 0
        newString = ""

        while count < len(first) :
            
            v = remainder + int(first[index]) 

            if count < len(second): 
                v += int(second[index])
                
            remainder = 0
            if v >= 10:
                remainder = 1
                v -= 10
            newString = str(v) + newString

            count += 1
            index -= 1

        return  newString if remainder != 1 else "1"+newString

