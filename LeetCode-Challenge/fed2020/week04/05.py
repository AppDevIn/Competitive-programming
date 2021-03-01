# 946. Validate Stack Sequences
#https://leetcode.com/problems/validate-stack-sequences/
class Solution:
    def validateStackSequences(self, pushed: [], popped: []) -> bool:

        push = []
        index = 0
        
        for pu in pushed:
            push.append(pu)

            while push and index < len(popped) and push[-1] == popped[index]:
                index += 1
                push.pop()

        return index == len(popped)

        

solution = Solution()

print(solution.validateStackSequences([0,2,1], [0,1,2]))


