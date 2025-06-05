class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            idx = find(x)
            idy = find(y)
            if idx == idy:
                return 

            if idx > idy:
                parent[idx] = idy
            else:
                parent[idy] = idx
                 

        for c in range(26):
            ch = chr(ord('a') + c)
            parent[ch] = ch

        for a, b in zip(s1, s2):
            union(a, b)
        
        result = ""
        for char in baseStr:
            result += find(char)

        return result








  
