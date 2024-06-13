class Solution:
    def insertionSort(self, value, arr):
        index = 0
        while index < len(arr) and value > arr[index]:
            index += 1
        arr.insert(index, value)
        
    def findEvenNumbers(self, digits: List[int]) -> List[int]:

        hashSet = {}
        even = []
        sortedDigitis = []
        arr = []
        for d in digits:
            if d not in hashSet:
                hashSet[d] = 1
                even.append(d)
                self.insertionSort(d, sortedDigitis)
            else:
                hashSet[d] = hashSet[d] + 1

        def helper(sum, count):

            if len(sum) == 3:
                if int(sum) % 2 == 0:
                    arr.append(int(sum))
                return 
            for d in sortedDigitis:
                if len(sum) == 0 and d  == 0:
                    continue
                
                if hashSet[d] - count.get(d, 0) > 0:
                    count[d] = count.get(d, 0) + 1
                    helper(sum+str(d), count)
                    count[d] = count.get(d, 0) - 1
        
        helper("", {})
        return arr

                
        
