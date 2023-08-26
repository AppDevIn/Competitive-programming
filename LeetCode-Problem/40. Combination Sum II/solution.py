class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidate, target, combination, index, result):
            if target == 0:
                result.append(combination[:])
                return
            if target < 0 or index >= len(candidate):
                return
            
            for i in range(index, len(candidate)):
                if i > index and candidate[i] == candidate[i-1]:
                    continue
                
                combination.append(candidate[i])
                dfs(candidate, target - candidate[i], combination, i + 1, result)
                combination.pop()
                
        candidates.sort() 
        result = []
        dfs(candidates, target, [], 0, result)
        return result

