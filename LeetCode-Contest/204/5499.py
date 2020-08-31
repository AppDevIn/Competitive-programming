# Detect Pattern of Length M Repeated K or More Times
import re

class Solution:
    def containsPattern(self, arr: [int], m: int, k: int) -> bool:
        value = ''
        unqiueArr = arr
        for x in arr:
            value += str(x)
        
        start = 1
        for x in unqiueArr:
            
            if m > 1:
                count = start
                for pos in range(1,m):
                    if(count >= len(unqiueArr)):
                        return False
                    x = str(x) + str(list(unqiueArr)[count])
                    count += 1
                

            v = re.search("("+str(x)+")"+"{"+str(k)+",}", value )

            start += 1
            if v:
                return True
            else:
                continue
        return False





arr = input()
m = int(input())
k = int(input())

arr = arr[1:len(arr)-1]
l = arr.split(',')
l = ''.join(l)
arr = [x for x in l]

s = Solution()
print(s.containsPattern(arr=arr, m=m, k=k))