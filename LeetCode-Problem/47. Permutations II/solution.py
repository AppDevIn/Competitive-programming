class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(nums, res, l):
            if nums == []:
                if l not in res:
                    res.append(l)
                return
            front = []
            while nums:
                val = nums.pop()
                dfs(front+nums, res, l + [val])                
                front.append(val)
        dfs(nums, res, [])
        return res
