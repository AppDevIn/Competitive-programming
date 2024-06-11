class Solution:
    def __init__(self):
        self.counter = {}

    def sumCounter(self, v):
        if v in self.counter:
            return self.counter[v]

        count = 0
        for i in range(v):
            count += i

        self.counter[v] = count
        return count

    def numberOfSubstrings(self, s: str) -> int:
        numberOfSubString = 0
        d = {}
        for a in s:
            numberOfSubString += 1
            if a not in d:
                d[a] = 1
            else:
                d[a] = d[a] + 1

        for v in d.values():
            if v > 1:
                numberOfSubString += self.sumCounter(v)

        return numberOfSubString

