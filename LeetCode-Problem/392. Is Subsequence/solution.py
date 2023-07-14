class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        count = 0
        for c in t:
            if count == len(s):
                break
            if c == s[count]:
                count += 1
        
        return count == len(s)

        
