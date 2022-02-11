# 567. Permutation in String
# https://leetcode.com/problems/permutation-in-string/

class RecursionTree(object):
    def checkInclusion(self, s1, s2) -> object:
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        s1 = [char for char in s1]
        return self.rcur(s1, 0, s2) != 0

    def rcur(self, s1, depth, k):
        value = 0
        if depth >= len(s1) - 1:
            print(f"Final value: {''.join(s1)}")
            if ''.join(s1) in k:
                value += 1
            return value
        first = s1[:depth]
        second = s1[depth:len(k)]
        third = s1[len(k):]
        for i in range(len(second)):
            print(f"Entered {s1}")
            print(f"Depth: {depth}")
            print(f"New Array: {s1[depth:]}")
            second[0], second[i] = second[i], second[0]
            s1 = first + second + third
            print(f"Swapped: {s1}")
            value += self.rcur(s1, depth + 1, k)
        return value


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False

        s1Arr = self.toOrd(s1)

        win_size = len(s1)
        hashSet = {}

        for i in range(len(s2)):
            new_arr = s2[i: win_size+i]
            if len(new_arr) < len(s1):
                return False
            s2Arr = self.toOrd(new_arr)
            if s2Arr == s1Arr:
                return True
            else:
                continue
        return False


    def toOrd(self, arr):
        s = [0] * 26
        for i in arr:
            s[ord(i) - ord('a')] += 1
        return s
