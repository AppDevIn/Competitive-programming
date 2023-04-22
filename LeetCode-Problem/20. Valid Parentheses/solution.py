class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        s = list(s)
        mapping = {"(": ")", "{": "}", "[": "]"}
        for index in range(len(s)):
            if stack == [] and s[index] not in mapping.keys():
                return False
            if s[index] in mapping.keys():
                stack.append(s[index])
                continue
            if s[index] != mapping[stack.pop()]:
                return False
    
        return stack == []
            
            
            

