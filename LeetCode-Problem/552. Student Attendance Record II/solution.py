class Solution:
    def checkRecord(self, n: int) -> int:

        MOD = 10**9 + 7
        memo = [[[-1] * 3 for _ in range(2)] for _ in range(n + 1)]

        def helper(n, attendance, late):

            if attendance > 1 or late >= 3:
                return 0
            if n == 0:
                return 1

            if memo[n][attendance][late] != -1:
                return memo[n][attendance][late]

            counts = helper(n - 1, attendance + 1, 0) % MOD
            counts = (counts + helper(n - 1, attendance, late + 1)) % MOD
            counts = (counts + helper(n - 1, attendance, 0)) % MOD

            memo[n][attendance][late] = counts
            return counts

        return helper(n, 0, 0)

