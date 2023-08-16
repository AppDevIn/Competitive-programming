class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        aplhaToNum = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}

        combinations = set([""])
        for d in digits:
            
            aplha = aplhaToNum[d]
            l = set()
            for c in combinations:
                l.add(c+aplha[len(aplha)-4])
                l.add(c+aplha[len(aplha)-3])
                l.add(c+aplha[len(aplha)-2])
                l.add(c+aplha[len(aplha)-1])
            combinations = l
        return combinations if "" not in combinations != "" else []

