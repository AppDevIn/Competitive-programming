class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:  
        arr.sort()
        d = {}
        minValue = None
        for i in range(len(arr)-1):
            key = abs(arr[i] - arr[i+1])
            if minValue == None or key < minValue: minValue = key
            if key not in d:
                d[key] = [(arr[i], arr[i+1])]
            else: d[key].append((arr[i], arr[i+1]))
            
        
        return d[minValue]
        
