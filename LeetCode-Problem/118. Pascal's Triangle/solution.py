class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        arr = []
        for count in range(numRows):
            lst = [1]


            if count >= 2:
                innerCount = 1
                for c in range(len(arr[-1])-1):
                    lst.append(arr[-1][c] + arr[-1][c+1])
                    innerCount += 1
                lst.append(1)
            elif count == 1:
                lst.append(1)
            arr.append(lst)
        
        return arr
