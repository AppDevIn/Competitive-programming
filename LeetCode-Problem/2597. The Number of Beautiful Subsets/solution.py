class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        subsets = []

        def isBeautiful(arr, num, k):

            for a in arr:
                if abs(a-num) == k:
                    return False
            
            return True        


        def helper(nums, arr, k):
            if len(arr) >= 1:
                subsets.append(arr)

            if nums == []:
                return

            for i in range(len(nums)):
                if len(arr) == 0:
                    helper(nums[i + 1::], arr + [nums[i]], k)
                elif isBeautiful(arr, nums[i], k):
                    helper(nums[i + 1::], arr + [nums[i]], k)
            return 
        helper(nums, [], k)
        
        return len(subsets)

