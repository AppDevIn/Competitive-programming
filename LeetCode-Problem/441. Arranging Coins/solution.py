class Solution:
    def arrangeCoins(self, n: int) -> int:

        rows, coins = 0, 1

        while n >= coins:
            n -= coins
            coins += 1
            rows += 1
        
        return rows

