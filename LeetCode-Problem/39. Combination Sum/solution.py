class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def df(candidate, target, l, res):
            if target == 0:
                res.append(l)
                return
            for i in range(len(candidate)):
                if candidate[i] > target:
                    continue 
                df(candidate[i:], target-candidate[i], l+[candidate[i]], res)
        df(candidates, target, [], res)
        return res


