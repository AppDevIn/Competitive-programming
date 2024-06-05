class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        d = {}
        ans = []
        for wordIndex in range(len(words)):
            temp = []
            for char in words[wordIndex]:
                if char not in ans and wordIndex != 0:
                    continue
                if wordIndex != 0:
                    ans.remove(char)
                temp.append(char)
            ans = temp
        return ans



            
        

                
