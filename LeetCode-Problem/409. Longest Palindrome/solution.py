class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = {}

        for c in s:
            hashmap[c] = hashmap[c] + 1 if c in hashmap else 1

        count, maxOdd = 0, 0

        for v in hashmap.values():
            if v%2 == 0:
                count += v
            elif v > 1:
                count += v - 1
                v -= v - 1
            
            if v%2 == 1 and v > maxOdd:
                maxOdd = v

        return count + maxOdd

