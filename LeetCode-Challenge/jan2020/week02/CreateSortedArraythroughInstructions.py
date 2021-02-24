def createSortedArray(instructions):

    gl = []
    total = 0
    for x in range(0, len(instructions)):
        if len(gl) == 0:
            gl.append(instructions[x])
        elif instructions[x] >= gl[len(gl) - 1]:
            gl.append(instructions[x])
        else:
            count = 0
            same = 1
            for j in range(0,len(gl)):
                
                count += 1
                if(instructions[x] == gl[j]):
                    same += 1

                elif instructions[x] < gl[j]:
                    gl.insert(j, instructions[x])
                    total += min(count-same,(len(gl) - count))
                    print(f"min({count-same}, {len(gl) - count}) = {min(count-same,(len(gl) - count))}")
                    same = 0
                    break
    return total



print(createSortedArray([1,2,3,6,5,4]))
print(createSortedArray([1,3,3,3,2,4,2,1,2]))
                


