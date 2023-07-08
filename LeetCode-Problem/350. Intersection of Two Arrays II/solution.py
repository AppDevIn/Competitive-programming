class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        returnee = []

        count1, count2 = 0,0
        while count1 < len(nums1) and count2 < len(nums2):

            if nums1[count1] == nums2[count2]:
                returnee.append(nums1[count1])
                del nums1[count1]
                del nums2[count2]
            elif nums1[count1] < nums2[count2]:
                count1 += 1
            elif nums1[count1] > nums2[count2]:
                count2 += 1
            
        return returnee


