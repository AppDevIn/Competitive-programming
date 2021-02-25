# https://leetcode.com/problems/score-of-parentheses/
# 856. Score of Parentheses
# Solution not my own from leetcode
def scoreOfParentheses(S):
    """
    :type S: str
    :rtype: int
    """

    stack = [0]
    
    for p in S:
        if p == "(":
            stack.append(0)
        else:
            value = stack.pop()
            stack[-1] += max(2 * value, 1)
            
    return stack.pop()