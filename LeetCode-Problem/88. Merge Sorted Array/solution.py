class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nIndex = n - 1
        mIndex = m - 1
        largeIndex = m + n - 1

        while nIndex >= 0:
            if mIndex >= 0 and nums1[mIndex] > nums2[nIndex]:
                nums1[largeIndex] = nums1[mIndex]
                mIndex -= 1
            else:
                nums1[largeIndex] = nums2[nIndex]
                nIndex -= 1
                
            largeIndex -= 1
            


       
