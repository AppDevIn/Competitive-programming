class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        lst = s.split(" ")
        hashMap = {}
        hashMap2 = {}
        if len(lst) != len(pattern):
            return False
        for count in range(len(lst)):
            if pattern[count] not in hashMap:
                hashMap[pattern[count]] = lst[count]
            elif pattern[count] in hashMap and hashMap[pattern[count]] != lst[count]:
                return False
            
            if lst[count] not in hashMap2:
                hashMap2[lst[count]] = pattern[count]
            elif lst[count] in hashMap2 and hashMap2[lst[count]] != pattern[count]:
                return False    
            
        
        return True


