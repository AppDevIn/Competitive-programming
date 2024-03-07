class Solution:

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = str2
        while len(res) != 0:
            size = len(res)
            if len(str1) % size == 0 and len(str2) % size == 0:
                str1Div = int(len(str1) / size)
                str2Div = int(len(str2) / size)

                if res * str1Div == str1 and res * str2Div == str2: return res
            res = res[0:-1]
        return res
        


        




