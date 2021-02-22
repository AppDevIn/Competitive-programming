
def recursive(X, Y, count, up , memeroization=[]):

    if up:
        if X > Y + 2 or X <= 0 or X in memeroization:
            return 100
        elif X == Y:
            return count
        
        count += 1
        memeroization.append(X)
        value = recursive(X*2, Y, count, up, memeroization)
        value2 = recursive(X-1, Y, count, up, memeroization)
        
        return min(value, value2)
        
    else: 
        
        return (X-Y) - 1 



    


def brokenCalc(X, Y):
    """
    :type X: int
    :type Y: int
    :rtype: int
    """
    value = recursive(X, Y, 0 , X < Y , [])
    print("🚀 ~ file: brokenCalculator.py ~ line 33 ~ value", value)
    

brokenCalc(1, 1000000000)