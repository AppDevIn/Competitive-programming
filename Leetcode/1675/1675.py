# 1675. Minimize Deviation in Array (Incomplete)
# https://leetcode.com/problems/minimize-deviation-in-array/

# 75/76
class Solution(object):
    def minimumDeviation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        arr = []

        while nums[0] % 2 != 0:
            value = nums[0] * 2
            nums[0] = int(value)
            nums.sort()
            arr.append(nums[-1] - nums[0])

        diff = nums[-1] - nums[0]
        while nums[-1] % 2 == 0:
            value = nums[-1] / 2
            nums[-1] = int(value)
            nums.sort()
            diff = min([diff, nums[-1] - nums[0]])
            arr.append(diff)

        return min(arr) if arr != [] else nums[-1] - nums[0]


s = Solution()
print(s.minimumDeviation([9, 4, 3, 6, 2]))
