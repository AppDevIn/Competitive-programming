class Solution:
        
    def duplicateZeros(self, arr: [int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        cancel = -1
        l = len(arr)
        for x in range(len(arr)):
            if(arr[x] == 0 and x != cancel):
                cancel = x+1
                arr.insert(x+1, 0)
        
        for _ in range(len(arr) - l):
            arr.pop()
        
        
   
