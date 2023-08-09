class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1: return s


        l = []
        row = 0
        reverse = False
        for c in s:
            if len(l) < numRows:l.append(c)
            else:l[row] = l[row] + c
            
            if reverse:row -= 1
            else: row += 1

            if row >= numRows-1: reverse = True
            if row <= 0: reverse = False
        return "".join(l)
