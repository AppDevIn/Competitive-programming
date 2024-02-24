class Solution:
    def merge(self, left_list, right_list): 
        left, right = 0, 0
        lst = []
        while left < len(left_list) and right < len(right_list):
            if left_list[left] < right_list[right]:
                lst.append(left_list[left])
                left += 1
            else:
                lst.append(right_list[right])
                right += 1
        return lst + left_list[left:] + right_list[right:]
                
                
    
    def sortArray(self, nums: List[int]) -> List[int]:
        
        if len(nums) == 1: return nums
        
        pivot = int(len(nums)/2)
        
        leftside =  self.sortArray(nums[:pivot])
        rightside = self.sortArray(nums[pivot:])
        return self.merge(leftside, rightside)
