class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxSize = max(candies)
        res = []
        while candies:
            value = candies.pop(0)
            res.append(value + extraCandies >= maxSize)
        return res


        
