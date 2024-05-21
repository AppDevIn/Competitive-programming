class Solution:
    def XORallArray(self, arr):
        sum = 0
        for a in arr:
            sum = sum ^ a
        return sum 

    def subsetXORSum(self, nums: List[int]) -> int:

        subsets = []
        def helper(arr, index, subset):
            if index == len(arr):
                subsets.append(subset)
                return
            helper(arr, index + 1, subset + [arr[index]])
            helper(arr, index + 1, subset)

        helper(nums, 0, [])
        sum = 0
        for subset in subsets:
            sum += self.XORallArray(subset) 
        print(sum)    
        return sum

