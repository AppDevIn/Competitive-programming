class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        
        seen = []
        xorSum = 0
        for num in nums:
            if num in seen:
                xorSum = xorSum ^ num
            else:
                seen.append(num)
        return xorSum
        
