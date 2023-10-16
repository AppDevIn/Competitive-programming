class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        stack = []
        tmp = ""
        for x in s[::-1]:
            
            if x == " ":
                res = tmp + " " +  res
                tmp = ""
                continue
            tmp += x
        return (tmp + " " + res).strip()
