class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 1: return s

        left, right = 0, len(s)
        count = 0
        maxCurr = ""
        while count < len(s) - 1:
            if left >= right:
                count += 1
                left = count
                right = len(s)  
                continue
            if s[left] == s[right-1] and s[left:right] == s[right-1:left:-1] + s[left] and len(maxCurr) < len(s[left:right]):
                maxCurr = s[left:right]
                count += 1
                left = count
                right = len(s)
                continue

            
            right -= 1
        return maxCurr

                

