# 169. Majority Element

# class Solution(object):
#     def majorityElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#
#         hashSet = {}
#         maxCount, maxValue = 0, 0
#
#         for x in nums:
#             count = hashSet.get(x, 0) + 1
#             hashSet[x] = count
#             if count >= maxCount:
#                 maxCount = count
#                 maxValue = x
#
#         return maxValue

# class Solution(object):
#     def majorityElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#
#         hashSet = {}
#
#         for x in nums:
#             count = hashSet.get(x, 0) + 1
#             hashSet[x] = count
#             if count > len(nums) / 2:
#                 return x


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        setted = set(nums)
        for x in setted:
            if nums.count(x) > len(nums) / 2:
                return x



s = Solution()
print(s.majorityElement([3, 2, 3]))
print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))
print(s.majorityElement([1]))
print(s.majorityElement([3,3,4]))
