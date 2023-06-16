class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        hashMap = {}

        for count in range(len(s)):

            if s[count] in hashMap.keys():
                if hashMap[s[count]] != t[count]:
                    return False
            elif t[count] in hashMap.values():
                return False
            else:
                hashMap[s[count]] = t[count]

        return True
