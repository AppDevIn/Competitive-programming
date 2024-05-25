class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        
        colorList = {}
        ballList = {}
        ans = []
        def existBall(ball, color):
            if ball in ballList:
                prevColor = ballList[ball]
                colorList[prevColor].remove(ball)
                if len(colorList[prevColor]) == 0:
                    del colorList[prevColor]
            
        
        for ball, color in queries:
            existBall(ball, color)
            if color not in colorList:
                colorList[color] = [ball]
                ballList[ball] = color
                ans.append(len(colorList))
            else:
                colorList[color].append(ball)
                ballList[ball] = color
                ans.append(len(colorList))
        return ans
                
        
        
