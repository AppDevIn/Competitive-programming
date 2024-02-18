class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        
        def helper(row, maxRow, lst):
            if row == maxRow: return lst
            
            ans = [1]
            for i in range(0,len(lst)-1):
                ans.append(lst[i] + lst[i+1])
            ans.append(1)
            
            return helper(row+1, maxRow, ans)
        
        return helper(0, rowIndex, [1])
            
                
        
        
