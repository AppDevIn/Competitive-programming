class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0]*len(temperatures)
        stack = [[temperatures[0], 0]]
        
        for index in range(1, len(temperatures)):
            
            while stack and temperatures[index] > stack[0][0]:
                v = stack.pop(0)
                res[v[1]] = index - v[1]
            stack.insert(0, [temperatures[index], index])
        return res
        
