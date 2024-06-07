class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        d = {}

        for word in dictionary:
            curr = d
            for index, char in enumerate(word):
                if char in curr and index == len(word)-1:
                    curr[char] = [True, curr[char][1], word]
                elif char in curr:
                    curr = curr[char][1]
                else:
                    curr[char] = [index==len(word)-1, {}, word]
                    curr = curr[char][1]
  
        ans = ""
        print(d)
        for word in sentence.split():
            index = 0
            if word[index] not in d:
                ans += word + " "
            else:
                curr = d[word[index]]
                index = 1
                while index < len(word):
                    if curr[0]:
                        word = curr[2]
                    elif word[index] in curr[1]:
                        curr = curr[1][word[index]]
                    else:
                        break
                    index += 1
                ans += word + " "


        return ans.strip()

        
