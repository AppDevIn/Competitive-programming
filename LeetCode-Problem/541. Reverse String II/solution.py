class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) <= k:
            return s[::-1]
        s = s[0:k][::-1] + s[k::]
        for i in range(2*k, len(s), 2*k):
            if k >= len(s):
                return s
            else: s = s[0:i] + s[i:i+k][::-1] + s[i+k::]
            
        return s
        
