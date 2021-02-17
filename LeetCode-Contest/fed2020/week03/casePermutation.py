def letterCasePermutation(S):
    """
    :type S: str
    :rtype: List[str]
    """
    lst = []
    def caseChange(subStr="" ,index = 0):

        if len(subStr) == len(S):
            lst.append(subStr)
        else:
            if S[index].isalpha():
                caseChange(subStr=subStr+S[index].swapcase(), index= index+1)
            caseChange(subStr=subStr+S[index], index= index+1)
    caseChange()
    return lst

print("🚀 ~ file: casePermutation.py ~ line 21 ~ letterCasePermutation(3z4)", letterCasePermutation("mQe"))


