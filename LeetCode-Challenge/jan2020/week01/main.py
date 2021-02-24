def canFormArray(arr: [int], pieces: [[int]]) -> bool:
    
    count = 0
    countWhile = 0
    breakCount = 0
    newArr = []
    if len(pieces) == 1:
        for x in pieces:
            for z in x:
                newArr.append(z)
    else:
        while len(newArr) != len(arr) :
            countWhile += 1
            for x in range(0,len(pieces)):
                if len(pieces[x]) > 1:
                    if arr[count] == pieces[x][0]:
                        for z in pieces[x]:
                            newArr.append(z)
                            count+=1     
                        pieces.pop(x)
                        break
                else:
                    if arr[count] == pieces[x][0]:
                        newArr.append(pieces[x][0])
                        pieces.pop(x)
                        count+=1
                        break
            if countWhile > count:
                return False


        
    return newArr == arr







#Test case

print(canFormArray([2,82,79,95,28], [[2],[82],[28],[79,95]])) #true
print(canFormArray([49,18,16], [[16,18,49]])) # false
print(canFormArray([100,2,98,28,44,55,37], [[28,46,57],[37,19,40,38]])) # false
print(canFormArray([91,4,64,78], [[78],[4,64],[91]])) # true



