class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        
        occurrences = []
        ans = []
        for i in range(len(nums)):
            if nums[i] == x:
                occurrences.append(i)
        
        
        for q in queries:
            if q <= len(occurrences) :
                ans.append(occurrences[q-1])
                
            else:
                ans.append(-1)
        
        return ans
                
        
