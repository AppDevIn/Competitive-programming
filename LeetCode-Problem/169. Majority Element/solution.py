class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        value = 0
        frequency = 0
        maxValue = 0
        maxFrequency = 0

        nums = sorted(nums)

        for v in nums:
            if v != value:
                frequency = 0
                value = v

            frequency += 1
            if frequency > maxFrequency:
                maxValue = value
                maxFrequency = frequency

        print(maxValue, maxFrequency)
        return maxValue

