class Solution:
    def countSegments(self, s: str) -> int:
        ans = 0
        for i,x in enumerate(s):
            if x != " " and i+1 != len(s) and s[i+1] == " ":
                ans += 1
            elif x != " " and i+1 == len(s):
                ans += 1
        return ans 
