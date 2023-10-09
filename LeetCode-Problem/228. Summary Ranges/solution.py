class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return nums
        tmp = [nums[0]]
        index = 0
        res = []
        while index <= len(nums)-1:

            if index != len(nums)-1 and nums[index] + 1 == nums[index+1]:
                tmp.append(nums[index+1])
            else:
                if len(tmp) > 1:
                    res.append(str(tmp[0])+"->"+str(tmp[-1]))
                else:
                    res.append(str(tmp[0]))
                
                if index != len(nums)-1:
                    tmp = [nums[index+1]]
            index += 1
        return res



        
