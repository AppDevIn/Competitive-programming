class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        sentences = []
        def helper(s, wordDict, sentence, arr):
            if len(s) == 0: 
                arr.append(sentence.strip())
                return
            
            for word in wordDict:
                if s[:len(word)] == word:
                    helper(s[len(word)::], wordDict, sentence+word+" ", arr)
            return 

        helper(s, wordDict, "", sentences)
        return sentences
