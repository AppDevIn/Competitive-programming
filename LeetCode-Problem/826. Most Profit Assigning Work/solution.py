class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort()
        dp = {}
        n = len(difficulty)

        for index in range(n):
            diff = difficulty[index]
            if diff in dp:
                dp[diff] = max(dp[diff],profit[index])
            else: dp[diff] = profit[index]
        
        difficulty = sorted(list(dp.keys()))
        profit = 0
        index = 0
        m = 0
        for w in worker:
            
            while index < len(difficulty) and w >= difficulty[index]:
                m = max(m, dp[difficulty[index]])
                index += 1
            
            profit += m
        
        return profit
                
