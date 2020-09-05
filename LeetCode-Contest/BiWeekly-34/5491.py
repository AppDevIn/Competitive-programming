import numpy as np

class Solution:
    def diagonalSum(self, mat: [[int]]) -> int:
        dict = {}

        for l in range(len(mat)):
                dict[f"{l},{l}"] = mat[l][l] 
        l=len(mat)-1
        for g in range(len(mat)):
                dict[f"{g},{l}"] = mat[g][l] 
                l = l -1

        #Test code
        
        for x in dict.keys():
            z,y = [int(t) for t in x.split(',')]
            mat[z][y] = 'x'
        mat = np.array(mat)
        print(mat)


        return sum(dict.values())


s = Solution()

print(s.diagonalSum(mat=[[5,10,5,4,8,18,14,19,7,14,7,11],
                        [17,18,13,3,16,16,11,6,6,2,15,9],[11,16,14,11,11,12,17,16,4,7,8,1],[8,18,4,7,16,11,12,16,9,18,10,15],[1,13,12,11,1,9,19,8,16,9,16,9],[20,12,10,1,19,16,17,7,7,16,6,2],[11,20,2,3,17,14,14,11,14,2,16,14],[3,1,19,2,15,4,11,17,1,4,5,2],[9,9,4,12,10,16,15,3,17,12,17,11],[10,4,4,1,5,16,16,18,2,7,16,1],[8,15,2,10,16,10,7,16,20,20,12,13],[11,10,11,16,15,1,12,10,17,8,13,16]]))
        