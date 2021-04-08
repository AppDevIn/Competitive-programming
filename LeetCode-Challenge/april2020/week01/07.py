# 1704. Determine if String Halves Are Alike
# https://leetcode.com/problems/determine-if-string-halves-are-alike/


class Solution:
    def countV(self, s: str):
        v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        count = 0
        for x in v:
            if x in s:
                count += s.count(x)
        return count

    def halvesAreAlike(self, s: str) -> bool:

        middle = int(len(s)/2)
        a, b = s[:middle], s[middle:]
        aC = self.countV(a)
        bC = self.countV(b)

        return aC == bC


s = Solution()
print(s.halvesAreAlike("textBook"))
