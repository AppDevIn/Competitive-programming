# 322. Coin Change
# https://leetcode.com/problems/coin-change/
# Pass till test case 46
class Solution:
    def coinChange(self, coins, amount: int) -> int:
        coins.sort()
        
        if amount == 0:
            return 0

        count = 0
        for x in coins[::-1]:
            if x <= amount:
                count += amount//x
                amount = (amount%x)
                if amount == 0:
                    return count
        return -1

s = Solution()
s.coinChange([1,3,5], 11)