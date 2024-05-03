class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        first, second = 0, 0
        total = len(nums1) + len(nums2)
        ISODD = total % 2 == 1
        target = int(total / 2)


        median = 0
        arr = []
        count = 0

        while first < len(nums1) and second < len(nums2):
            if nums1[first] < nums2[second]:
                arr.append(nums1[first])
                first += 1
            else: 
                arr.append(nums2[second])
                second += 1
            
            if len(arr)-1 == target:
                return arr[target] if ISODD else (arr[target]+arr[target-1]) / 2




        if first >= len(nums1):
            arr += nums2[second:]
        elif second >= len(nums2):
            arr += nums1[first:]

        return arr[target] if ISODD else (arr[target]+arr[target-1]) / 2
            

