class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr = []
        for count in range(rowIndex+1):
            lst = [1]

            if count >= 2:
                innerCount = 1
                for c in range(len(arr)-1):
                    lst.append(arr[c] + arr[c+1])
                    innerCount += 1
                lst.append(1)
            elif count == 1:
                lst.append(1)
            arr = lst
        
        return arr
