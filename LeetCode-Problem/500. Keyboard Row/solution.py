class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        res = []
        for w in words:
            ori = w
            w = w.lower()
            row = 2
            if w[0] in keyboard[0]:
                row = 0
            elif w[0] in keyboard[1]:
                row = 1
            Invalid = True
            for c in w:
                if c not in keyboard[row]:
                    Invalid = False
                    break
            if Invalid:
                res.append(ori)
        return res



        
