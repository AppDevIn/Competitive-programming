class Solution:
    def insertionSort(self, value, arr):
        index = 0
        while index < len(arr) and value < arr[index]:
            index += 1
        arr.insert(index, value)

    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        sortedArr = []
        nameToHeight = {}

        for i in range(len(names)):
            self.insertionSort(heights[i], sortedArr)
            nameToHeight[heights[i]] = names[i]

        for i in range(len(sortedArr)):
            sortedArr[i] = nameToHeight[sortedArr[i]]
        return sortedArr

