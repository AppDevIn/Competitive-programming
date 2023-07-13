class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashmap = {}

        for c in s:
            if c in hashmap:
                hashmap[c] = hashmap[c] + 1
            else:
                hashmap[c] = 1

        for c in t:
            if c in hashmap and hashmap[c] == 0:
                return c
            elif c in hashmap:
                hashmap[c] = hashmap[c] - 1
            else:
                return c
