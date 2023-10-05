# 520. Detect Capital

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

 

Example 1:
```
Input: word = "USA"
Output: true
```
Example 2:
```
Input: word = "FlaG"
Output: false
 ```

Constraints:

1 <= word.length <= 100
word consists of lowercase and uppercase English letters.

# Solution
First Attempted 
```Python
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.upper() == word or word[0].upper()+word[1::].lower() == word or word.lower() == word
```
Second Attempt
```Python
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
```
