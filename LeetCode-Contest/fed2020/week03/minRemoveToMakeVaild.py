def minRemoveToMakeValid(s):
    """
    :type s: str
    :rtype: str
    """
    openBracket = []
    closeBracket = []
    normal = []
    s = [c for c in s]

    for index in range(len(s)):
        if (s[index] == "("):
            openBracket.append(index)
        elif (s[index] == ")" and len(openBracket) > len(closeBracket)):
            closeBracket.append(index)
        elif(s[index] != "(" and s[index] != ")"):
            normal.append(index)

    minValue = min(len(openBracket), len(closeBracket))

    remove = openBracket[0:minValue] + closeBracket[0:minValue] + normal

    newString = ""
    for i in range(len(s)):
        if(i in remove):
            newString += s[i]

    return newString


print("🚀 ~ file: minRemoveToMakeVaild.py ~ line 21 ~ minRemoveToMakeValid('(a(b(c)d))",
      minRemoveToMakeValid("lee(t(c)o)de)"))
