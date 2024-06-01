class Solution:
    def scoreOfString(self, s: str) -> int:

        i, j = 0, 1
        total = 0
        while j < len(s):
            total += abs(ord(s[i]) - ord(s[j]))
            i, j = j, j+1

        return total

