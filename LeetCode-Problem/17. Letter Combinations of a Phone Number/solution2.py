class Solution:
    def __init__(self):
        self.aplhaToNum = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}

    def letterCombinations(self, digits: str) -> List[str]:

        IS_DIGITS_EMPTY = len(digits) == 0
        def helper(combinations, digits):
            if len(digits) == 0:
                self.arr.append(combinations)
                return 
            
            digit = digits[0]
            helper(combinations+self.aplhaToNum[digit][0], digits[1::])
            helper(combinations+self.aplhaToNum[digit][1], digits[1::])
            helper(combinations+self.aplhaToNum[digit][2], digits[1::])
            if digit in ["7", "9"]:
                helper(combinations+self.aplhaToNum[digit][3], digits[1::])
        
        self.arr = []
        if not IS_DIGITS_EMPTY:
            helper("", digits)

        return self.arr

        

        
            

