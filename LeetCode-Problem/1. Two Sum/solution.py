class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliment = {}
        for i,x in enumerate(nums):
            num = target - x
            if num in compliment:
                return [i, compliment[num]]
            else:
                compliment[x] = i
