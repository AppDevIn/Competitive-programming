class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        hashMap = {}
        binMap = {}


        for count in range(len(nums)):
            
            if nums[count] in hashMap and not binMap[nums[count]]:
                if abs(hashMap[nums[count]] - count) <= k:
                    binMap[nums[count]] = True
                else:
                    binMap[nums[count]] = False

            if nums[count] not in binMap:
                binMap[nums[count]] = False
            

            hashMap[nums[count]] = count
        
        return True in binMap.values()
        
                
