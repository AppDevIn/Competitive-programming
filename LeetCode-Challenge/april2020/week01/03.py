class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        count = 0
        for x in s:
            if x == "(":
                stack.append(x)
            elif x == ")" and len(stack) != 0:
                stack.pop()
                count += 2
        return count


s = Solution()
s.longestValidParentheses(")()())")
