def swap_arr(arr, swap):
    tmp = arr[swap-1]
    arr[swap-1] = arr[swap]
    arr[swap] = tmp
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}
        
        for i in nums:
            if i in d: d[i] = d[i] + 1
            else: d[i] = 1
                
        arr = list(d.values())
        keys = list(d.keys())
        index = 1
        
        while index < len(arr):
            if arr[index] < arr[index-1]: 
                index += 1
                continue 
            swap = index
            while swap != 0 and arr[swap] > arr[swap-1]:
                swap_arr(arr, swap)
                swap_arr(keys, swap)
                swap -=1
            index += 1
        return keys[0:k]
                
                
        
