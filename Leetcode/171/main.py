# 171. Excel Sheet Column Number
# https://leetcode.com/problems/excel-sheet-column-number/

class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """

        total = ord(columnTitle[0]) - 64
        columnTitle = columnTitle[1::]
        for c in columnTitle:
            total = (total * 26) + (ord(c) - 64)

        return total


s = Solution()
print(s.titleToNumber("BA"))
