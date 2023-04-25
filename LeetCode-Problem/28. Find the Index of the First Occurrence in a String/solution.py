class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        sizeOfNeedle = len(needle)
        for index in range(len(haystack)):
            if haystack[index] == needle[0] and haystack[index:index+sizeOfNeedle] == needle:
                    return index
        return -1
