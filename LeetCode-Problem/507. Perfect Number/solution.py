import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        value = 0
        res = []
        index = num
        while index > 1:
            i = math.ceil(index / 2)
            if num % i == 0: 
                res.append(i)
            index = i
        if sum(res) != num:
            return False
        for i in range(1, int(num/2)+1):
            if num % i == 0 and i not in res:
                return False
                
        return True
        
