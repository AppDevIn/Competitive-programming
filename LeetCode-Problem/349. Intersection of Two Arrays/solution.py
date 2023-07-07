class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        count1, count2 = 0, 0
        
        hashmap = {}
        returnee = set()
        while count1 < len(nums1):
            if nums1[count1] not in hashmap:
                hashmap[nums1[count1]] = [True, False]
            else:
                hashmap[nums1[count1]][0] = True
            
                
            if hashmap[nums1[count1]][0] and hashmap[nums1[count1]][1]:
                returnee.add(nums1[count1])
                
            count1 += 1
            
        while count2 < len(nums2):
    
            if nums2[count2] not in hashmap:
                hashmap[nums2[count2]] = [False, True]
            else:
                hashmap[nums2[count2]][1] = True
                 
            if hashmap[nums2[count2]][0] and hashmap[nums2[count2]][1]:
                returnee.add(nums2[count2])
                
            count2 += 1
            
        
        return returnee
