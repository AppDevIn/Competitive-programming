def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
class Solution:
    def heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        if largest != i:
            swap(arr, i, largest)
            self.heapify(arr, n, largest)
    
    def buildHeap(self, arr):
        n = len(arr)
        startIdx = n // 2 - 1
        for i in range(startIdx, -1, -1):
            self.heapify(arr, n, i)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        self.buildHeap(nums)
        
        for i in range(n-1, n-1-k, -1):
            swap(nums, 0, i)
            self.heapify(nums, i, 0)
        return nums[n-k]
