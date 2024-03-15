class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        values = [(0,0)]
        ans = [""]
        left, right  = values[0]
        while left < n or right < n or right < left:
            
            left, right = values.pop(0)
            para = ans.pop(0)
            
            if left < n:
                values.append((left+1, right))
                ans.append(para+"(")
            if right < left:
                values.append((left, right+1))
                ans.append(para+")")
            

        return ans + [para]
        
            
            
            
            
