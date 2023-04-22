class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key=len)
        
        current = strs[0]
        for index in range(1, len(strs)):
            for x in range(len(current), -1, -1):
                print(strs[index])
                print(current)
                if current[0:x] == strs[index][0:x] or current[0:x] == strs[index][x:0]:
                    current = current[0:x]
                    break
        return current


