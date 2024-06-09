class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        ans = [1]* n
        
        for _ in range(k):
            s = 0
            tmp = []
            for i in ans:
                s = (s + i) % MOD
                tmp.append(s)
            ans = tmp
        return ans[-1]
        
