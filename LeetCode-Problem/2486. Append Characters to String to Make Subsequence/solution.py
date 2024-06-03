class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        length = len(t)

        pS, pT = 0, 0
        
        while pS < len(s) and pT < length:
            if s[pS] == t[pT]:
                pT += 1
            pS += 1
        
        return length - pT
        
