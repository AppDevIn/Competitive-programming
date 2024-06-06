class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        ans = arrays[0]

        for arr in arrays[1::]:
            index = 0
            arrIndex = 0
            while index < len(ans) and arrIndex < len(arr):
                if ans[index] == arr[arrIndex]:
                    index += 1
                    arrIndex += 1
                elif ans[index] < arr[arrIndex]:
                    ans.pop(index)
                elif ans[index] > arr[arrIndex]:
                    arrIndex += 1
            ans = ans[0:index]
                    
                    
                
        return ans
