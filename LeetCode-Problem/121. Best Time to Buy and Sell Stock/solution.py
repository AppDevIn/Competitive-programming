class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxProfit = 0
        while right < len(prices):
            value = prices[right] - prices[left]
            if prices[left] < prices[right]:
                maxProfit = max(value, maxProfit)
            else:
                left = right
            right += 1
        return maxProfit
