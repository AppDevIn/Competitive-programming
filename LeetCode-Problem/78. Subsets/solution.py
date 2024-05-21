class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        def helper(arr, index, subset):
            if index == len(arr):
                subsets.append(subset)
                return
            helper(arr, index + 1, subset + [arr[index]])
            helper(arr, index + 1, subset)

        helper(nums, 0, [])
        return subsets
        
