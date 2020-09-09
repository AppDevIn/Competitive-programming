class Solution:
    def findMaxConsecutiveOnes(self, nums: [int]) -> int:
        lst = list(map(str,nums))
        s = ''.join(lst)
        x = s.split("0")
        
        max = 0
        for i in x:
            if(len(i) > max):
                max = len(i)
        return max
            
            
        
s = Solution()

result = s.findMaxConsecutiveOnes([1,1,0,1,1,1])        

print(result)
        
