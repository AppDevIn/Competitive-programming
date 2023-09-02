class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        uuid = {}
        for s in strs:
            holder = []

            for a in s:
                holder.append(a)
            holder.sort()
            key = ''.join(holder)
            
            if key in uuid:
                uuid[key].append(s)
            else:
                uuid[key] = [s]
        return uuid.values()
        
