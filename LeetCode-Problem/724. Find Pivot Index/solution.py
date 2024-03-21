class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        calAssetLeft = [0]
        calAssetRight = [0]

        for n in nums[:-1]:
            calAssetLeft.append(calAssetLeft[-1]+n)
        for n in nums[::-1][:-1]:
            calAssetRight.append(calAssetRight[-1]+n)

        rangeRight = len(calAssetRight)-1
        for i, n in enumerate(nums):

            if calAssetRight[rangeRight-i] == calAssetLeft[i]:
                return i

        return -1
        
