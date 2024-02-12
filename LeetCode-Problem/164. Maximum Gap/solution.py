
def counting_sort(lst, place_value):
    counts = [0]*10
    
    for x in lst:
        index = (x//place_value) % 10
        counts[index] = counts[index] + 1
        
    starting_index = 0
    for i, count in enumerate(counts):
        counts[i] = starting_index
        starting_index += count
        
    sorted_list = [0] *len(lst)
    
    for e in lst:
        index = (e//place_value) % 10
        sorted_list[counts[index]] = e
        
        counts[index] += 1
    for i,e in enumerate(sorted_list):
        lst[i] = e

    

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        maxElement = max(nums)
        place_value = 1
        while place_value <= maxElement:
            counting_sort(nums, place_value)
            place_value *= 10
        
        first, second = 0, 1
        maxGap = 0
        while second < len(nums):
            diff = nums[second] - nums[first]
            if diff > maxGap: maxGap = diff
            first = second
            second += 1
        return maxGap
                
            
            
            
        
        
