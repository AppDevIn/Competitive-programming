class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        h = copy.copy(score)
        h.sort(reverse=True)
        
        for index in range(len(score)):
            i = h.index(score[index]) + 1
            if i == 1: score[index] = "Gold Medal"
            elif i == 2: score[index] = "Silver Medal"
            elif i == 3: score[index] = "Bronze Medal"
            else: score[index] = f"{i}"
        return score

