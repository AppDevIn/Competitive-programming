class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        dicM = {}
        for m in magazine:
            if m in dicM:
                dicM[m] = dicM[m] + 1
            else:
                dicM[m] = 1
  
        for r in ransomNote:
            if r in dicM and dicM[r] >= 1:
                dicM[r] = dicM[r] - 1
                print(dicM)
            else: return False
        return True

