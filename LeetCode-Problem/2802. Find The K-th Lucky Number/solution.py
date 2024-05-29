class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        k = k + 1

        kth_lucky_num = ""
        while k > 1:
            kth_lucky_num = "".join((("7" if k & 1 else "4"), kth_lucky_num))
            k >>= 1
        return kth_lucky_num
