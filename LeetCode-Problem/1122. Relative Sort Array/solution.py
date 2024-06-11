class Solution:
    def insertSort(self, arr, value):
        index = 0
        while index < len(arr) and value > arr[index]:
            index += 1
        arr.insert(index, value)
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        orderDic = {}
        notInArr = []
        for a in arr1:
            if a not in orderDic and a in arr2:
                orderDic[a] = 1
            elif a not in arr2:
                self.insertSort(notInArr, a)
            else:
                orderDic[a] = orderDic[a]+1
        
        relativeOrder = []
        for a in arr2:
            relativeOrder += [a]*orderDic[a]
        
        return relativeOrder + notInArr
