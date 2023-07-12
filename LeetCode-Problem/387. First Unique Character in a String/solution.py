class Solution:
    def firstUniqChar(self, s: str) -> int:

        for count in range(len(s)):
            if s[count] not in s[0:count] + s[count+1:len(s)]:
                return count 
        return -1

