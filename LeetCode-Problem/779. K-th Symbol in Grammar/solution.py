class Solution:

    def kthGrammar(self, n: int, k: int, value=0) -> int:

        length = 2**(n-1)
        mid = length // 2

        if length == 1:
            return value

        if k > mid:
            return self.kthGrammar(n-1, k-mid, 0 if value == 1 else 1)
        else:
            return self.kthGrammar(n-1, k, value)

