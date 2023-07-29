class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort(reverse=True)
        s.sort(reverse=True)

        count, index = 0, 0
        while count < len(s) and index < len(g):
            if s[count] >= g[index]:
                count += 1
            index += 1
        return count
