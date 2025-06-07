import heapq

class Solution:
    def clearStars(self, s: str) -> str:
        s = list(s)  
        min_heap = []
        size_dic = {}
        for i, c in enumerate(s):
            if c == '*':
                smallest_char = heapq.heappop(min_heap)
                s[size_dic[smallest_char].pop()] = ''  
            else:
                if c in size_dic:
                    size_dic[c].append(i)
                else:
                    size_dic[c] = [i]
                heapq.heappush(min_heap, c)

        return ''.join([ch for ch in s if ch != '*'])
