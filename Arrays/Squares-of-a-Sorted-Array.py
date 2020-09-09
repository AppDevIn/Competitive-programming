class Solution:
    def sortedSquares(self, A: [int]) -> [int]:
        lst = list(map(lambda x:x*x, A))
        lst.sort()
        return lst

s = Solution()

print(s.sortedSquares([-4,-1,0,3,10]))


