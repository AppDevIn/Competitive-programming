# Some kind of stable sort
# def _sort():continue
class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        unsortedQueries = copy.deepcopy(queries)
        queries.sort(key=lambda x: x[1], reverse=True)
        ans = [0] * len(unsortedQueries)
        original = []
        for i in range(len(nums)):
            original.append((nums[i], i))
            nums[i] = (nums[i], i)

        while queries != []:
            nums = original
            for index in range(len(nums)):
                value = max(0,len(nums[index][0])-queries[0][1])
                nums[index] = (nums[index][0][value:], nums[index][1])
            nums.sort()
            for r in [i for i, x in enumerate(unsortedQueries) if x == queries[0]]:
                ans[r] = nums[queries[0][0]-1][1]
            value = queries[0]
            while value in queries:
                queries.remove(value)
        return ans
            
        
                                        
        
        
        
        
        
