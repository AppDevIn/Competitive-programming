class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        n = int(math.sqrt(c))


        for i in range(n+1, -1, -1):
            value = c - (i * i)
            
            if value >= 0 and math.sqrt(value) == int(math.sqrt(value)):
                 return True
            
        return False


        
