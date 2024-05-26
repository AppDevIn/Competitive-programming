class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        count = 1
        prev = word[0]
        for c in word[1::]:
            if c != prev or count == 9:
                
                comp += f'{count}{prev}'
                prev = c
                count = 1
            else:
                count += 1
        comp += f'{count}{prev}'
        return comp
        
