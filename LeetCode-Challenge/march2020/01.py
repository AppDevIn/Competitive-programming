# 575. Distribute Candies
# https://leetcode.com/problems/distribute-candies/
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        
        value = len(candyType) / 2
        maxTypes = len(set(candyType))
        
        if value > maxTypes:
            return int(maxTypes)
        return int(value)
        
        