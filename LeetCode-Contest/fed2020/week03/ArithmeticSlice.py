def numberOfArithmeticSlices(A):
    """
    :type A: List[int]
    :rtype: int
    """
    ans = 0
    count = 1
    for i in range(2,len(A)):
  
        if(A[i] - A[i-1]) == (A[i-1] - A[i - 2]):
            ans += count 
            count += 1
        else:
            count = 1
    return ans
        

print("🚀 ~ file: ArithmeticSlice.py ~ line 16 ~ numberOfArithmeticSlices([1,2,3,4])", numberOfArithmeticSlices([1,2,3,4]))
    
