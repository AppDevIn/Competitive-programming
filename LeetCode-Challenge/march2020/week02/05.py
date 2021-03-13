# 1461. Check If a String Contains All Binary Codes of Size K
# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        for r in range(0, pow(2,k)):
            binValue = bin(r)[2:]
            binValue = "0" * (k - len(binValue))  + binValue
            
            if binValue in s:
                continue 
            else:
                return False
        return True
            
            