class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        modSeen = {0:-1}
        total_sum = 0

        for i in range(len(nums)):
            total_sum += nums[i]
            mod = total_sum % k

            if mod in modSeen:
                if i - modSeen[mod] > 1:
                    return True
            else:
                modSeen[mod] = i

        return False

