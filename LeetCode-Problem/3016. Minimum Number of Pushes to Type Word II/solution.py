class Solution:
    def minimumPushes(self, word: str) -> int:
        d = {}

        for w in word:
            if w in d:
                d[w] = d[w] + 1 
            else:
                d[w] = 1
        d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        
        pushes = 0
        counter = 1
        for v in d.values():
            division = counter / 8
            remainder = division % 1
            increaseBy = division // 1
            if remainder > 0:
                increaseBy += 1
            pushes += v * int(increaseBy)
            counter += 1 


        return pushes
