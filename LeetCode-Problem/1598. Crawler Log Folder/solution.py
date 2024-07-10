class Solution:
    def minOperations(self, logs: List[str]) -> int:

        count = 0
        for l in logs:
            
            if l[:2] == ".." and count != 0:
                count -= 1
            elif l[:1] != ".":
                count += 1
        return count 

        
