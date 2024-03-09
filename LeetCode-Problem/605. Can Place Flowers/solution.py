class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1 and not flowerbed[0]: return True

        i = 0
        while i < len(flowerbed)-1:
            if flowerbed[i] == 1:
                i += 1
                continue
            if i == 0 and not flowerbed[1]:
                flowerbed[0] = 1
                n-=1
            elif i == len(flowerbed)-2 and not flowerbed[len(flowerbed)-1]: 
                flowerbed[i+1] = 1
                n-=1
            elif not flowerbed[i-1] and not flowerbed[i+1]:
                flowerbed[i] = 1
                n-=1
            i+=1
        return n <= 0
        
            




        
