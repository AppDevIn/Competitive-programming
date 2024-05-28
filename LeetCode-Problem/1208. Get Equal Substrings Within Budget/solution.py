class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        diffs = []
        for i in range(len(s)):
            diffs.append(abs(ord(s[i])-ord(t[i])))

        start = 0
        currentCost = 0
        max_length = 0
        for i in range(len(diffs)):
            currentCost += diffs[i]
            while currentCost > maxCost:
                currentCost -= diffs[start]
                start += 1

            max_length = max(max_length, i-start+1)
            

        return max_length
        
