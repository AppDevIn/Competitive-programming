def validMountainArray(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    if len(arr) < 3 : return False
    
    curr = 0
    increase = False
    decrease = False
    for x in range(len(arr)):
        if x == 0:
            curr = arr[x]
            continue 
        
        if curr == arr[x]:
            return False
        elif curr < arr[x] and decrease:
            return False
        elif curr < arr[x]:
            curr = arr[x]
            increase = True
        elif curr > arr[x] and increase:
            curr = arr[x]
            decrease = True
    return increase and decrease


print(validMountainArray([0,3,2,1]))