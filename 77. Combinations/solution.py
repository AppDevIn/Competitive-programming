class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        

        l = []
        def recur(m, r, start, s):
            if m == k:
                l.append(s)
                return
            for i in range(start, r+1):
                recur(m+1, n, i+1, s+[i])



        for i in range(1, n+1):
            recur(1, n, i+1,[i])
        return l
