class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

        remainder = 0
        totalWaterBottle = numBottles
        while numBottles >= numExchange:
            bottlesFilled = numBottles // numExchange
            remainder = numBottles % numExchange
            numBottles = bottlesFilled + remainder
            totalWaterBottle += bottlesFilled
        return totalWaterBottle
        
        
