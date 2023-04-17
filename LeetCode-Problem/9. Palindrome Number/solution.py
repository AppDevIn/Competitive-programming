class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_num = str(x)
        return string_num[::-1] == string_num
