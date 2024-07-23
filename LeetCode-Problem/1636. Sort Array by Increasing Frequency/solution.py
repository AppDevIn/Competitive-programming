class Solution:
    def insertionSort(self, dict, arr, key):
        index = 0
        while index < len(arr) and (dict[key] > dict[arr[index]] or (dict[key] == dict[arr[index]] and key < arr[index])):
            index += 1
        arr.insert(index, key)

    def frequencySort(self, nums: List[int]) -> List[int]:

        numSizeDic = {}

        for n in nums:
            numSizeDic[n] = numSizeDic.get(n, 0) + 1
        
        sortedArr = []
        for n in numSizeDic.keys():
            self.insertionSort(numSizeDic, sortedArr, n)
        
        ans = []
        for s in sortedArr:
            ans += [s] * numSizeDic[s]

        return ans


