class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hashMapS = {}
        hashMapT = {}
        for count in range(len(s)):
            if s[count] in hashMapS:
                hashMapS[s[count]] = hashMapS[s[count]]+1
            else:
                hashMapS[s[count]] = 0

            if t[count] in hashMapT:
                hashMapT[t[count]] = hashMapT[t[count]]+1
            else:
                hashMapT[t[count]] = 0        

        return hashMapS == hashMapT

