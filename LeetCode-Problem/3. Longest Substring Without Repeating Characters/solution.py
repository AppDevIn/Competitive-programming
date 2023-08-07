class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxSubString = 1
        for index, start in enumerate(s):
            subString = start
            count = 1
            for append in s[index+1::]:
                if append in subString: break 
                subString += append
                count += 1
                if count > maxSubString:
                    maxSubString = count 

        return maxSubString if len(s) != 0 else 0class Solution:
