class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(nums, res, l):
            if nums == []:
                res.append(l)
                return
            front = []
            while nums:
                val = nums.pop()
                dfs(front+nums, res, l + [val])                
                front.append(val)
        dfs(nums, res, [])
        return res
