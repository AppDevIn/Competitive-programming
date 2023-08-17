class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def df(left, right, s):
            if len(s) == n * 2: 
                res.append(s)
                return
            
            if left < n:
                df(left + 1, right, s + "(")
            
            if right < left:
                df(left, right + 1, s + ")")
            
        
        res = []
        df(0, 0, "")
        return res
