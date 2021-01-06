
# def twoSum(self, nums: List[int], target: int) -> List[int]:        
#     for i in range(0, len(nums)):
#         for x in range(0, len(nums)):
#             if (i != x) and nums[i] + nums[x] == target:
#                 return [i, x]
    


def s(self, i:int, x:int, nums: List[int], target:int):
    if x == len(nums):
        return 0
    elif i != x and nums[i] + nums[x] == target:
        return [i, x]
    

    if x != len(nums):
        if i == x:
            return self.s(i, x+2, nums, target)
        else: 
            return self.s(i, x+1, nums, target)
    
                
    
    
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for x in range(0, len(nums)):
        output = self.s(x, 0, nums, target)
        if output  != 0:
            return output