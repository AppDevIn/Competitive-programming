class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # Current Value * 26 + current number of char
        curr = ord(columnTitle[0]) - 64
        for char in columnTitle[1::]:
            curr = curr * 26 + (ord(char) - 64)


        return curr

