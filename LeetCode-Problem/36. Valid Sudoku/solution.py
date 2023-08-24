class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        threeByThree = {}
        cols = [[], [], [], [], [], [], [], [], []]

        for index,row in enumerate(board):
            
            for i, col in enumerate(row):
                if col in row[i+1::] and col != ".":
                    return False
                if col in cols[i] and col != ".":
                    print("Failed to gave the same col")
                    return False
                else:
                    cols[i].append(col)
                key = f"{i//3}{index//3}"
                if key in threeByThree:
                    if col in threeByThree[key] and col != ".":
                        print("Failed by 3 by 3")
                        return False
                    else: threeByThree[key].append(col)

                    
                else:
                    threeByThree[key] = [col]
        return True
                

                
