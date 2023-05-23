class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = ""
        queue = ""

        for char in s:
            if char.isalnum():
                queue += char.lower()
                stack = char.lower() + stack
        return stack == queue

