class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        size = 0
        for char in s[::-1]:
            if char == " " and size > 0:
                return size
            if char == " ":
                size = 0
            else:
                size += 1
        return size
