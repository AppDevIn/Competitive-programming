
def findKthPositive(arr: [int], k: int) -> int:
    larr = []
    for x in range(1, arr[len(arr)-1]+(k+3)):
        if x not in arr:
            larr.append(x)
    print(larr)
    return larr[k-1]


print(findKthPositive([2,3,4,7,11],5))
print(findKthPositive([1,2,3,4],2))