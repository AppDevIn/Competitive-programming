class Solution:
    def maxDifference(self, s: str) -> int:
        d = {}
        minimum, maximum = len(s) + 1, 0
        for c in s:
            if c in d:
                d[c] = d[c] + 1
            else:
                d[c] = 1
        
        for k in d.keys():
            
            if d[k] % 2 != 0:
                maximum = max(maximum, d[k])
            else:
                minimum = min(minimum, d[k])
            
        return maximum - minimum
            

        
