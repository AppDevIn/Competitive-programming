class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
   
        nums.sort()
        closet = float("inf")


        for i in range(len(nums)):
            

            j, k = i + 1, len(nums) - 1

            while j < k:
                s = nums[i]+nums[j]+nums[k]
                
                if s < target: j += 1
                else:k -= 1
                if abs(s - target) < abs(closet - target):
                    closet = s
                    
        return closet

        
