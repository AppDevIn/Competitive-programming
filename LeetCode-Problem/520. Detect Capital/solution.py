class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        allLettersCapital = True
        allLettersNotCapital = True
        onlyFIrstLetterIsCapital = True

        for i,c in enumerate(word):
            
            if ord(c) > 90: allLettersCapital = False
            else: allLettersNotCapital = False
            if ord(c) > 90 and i == 0: onlyFIrstLetterIsCapital = False
            if ord(c) <= 90 and i != 0: onlyFIrstLetterIsCapital = False
        
        return allLettersCapital or allLettersNotCapital or onlyFIrstLetterIsCapital
