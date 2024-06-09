class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        modSeen = {0:0}
        total_sum = 0
        count = 0
        for i in range(len(nums)):
            total_sum += nums[i]
            mod = total_sum % k

            if mod in modSeen or mod == 0:
                modSeen[mod] = modSeen[mod] + 1
                count += modSeen[mod]
            else:
                modSeen[mod] = 0

        return count

