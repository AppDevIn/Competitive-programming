case_input = int(input())
input()

def findPeak(height_array, n, length):
    
    for index in range(n, len(height_array)):
        
        if length == 1:
            return -1
        elif index > length-1 or index < 0:
            return -1
        elif index >= length-1:
            return index
        elif height_array[index] + 1 == height_array[index+1]:
            continue 
        else:
            return index
            


for i in range(case_input):
    length = int(input())
    height_array = list(map(lambda x: int(x),input().split(" ")))
    input()

    value = [-1, -1]

    for x in range(len(height_array)):
        if height_array[x] == 1:
            index = findPeak(height_array, x, length)
            if height_array[index] > value[0] and index != -1:
                
                value = [height_array[index], index]

    if value[1] == -1:

        height_array.reverse()
        for x in range(len(height_array)):
            index = findPeak(height_array, x, length)
            if height_array[index] > value[0] and index != -1:
                print(index)
                value = [height_array[index], index]
        
    print(f'{value[0]} {value[1]}')