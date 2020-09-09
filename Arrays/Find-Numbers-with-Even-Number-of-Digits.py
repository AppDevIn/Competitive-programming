class Solution:
     def findNumbers(self, nums: [int]) -> int:
        
        count = 0
        for n in nums:
            if(len(str(n))%2 == 0):
                count += 1
        return count 
                


s = Solution()

result = s.findNumbers([12,345,2,6,7896])

print(result)





