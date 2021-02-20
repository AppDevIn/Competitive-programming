def minRemoveToMakeValid(s):
    """
    :type s: str
    :rtype: str
    """
    openBracket = []
    closeBracket = []

    s = [c for c in s]

    for index in range(len(s)):
        if (s[index] == "("):
            openBracket.append(index)
        elif (s[index] == ")" and len(openBracket) > len(closeBracket)):
            closeBracket.append(index)

    minValue = min(len(openBracket), len(closeBracket))

    remove = openBracket + closeBracket
    for i in range(0, minValue):
        remove.append(openBracket[i])
        remove.append(closeBracket[i])

    for i in range(len(s)):
        if((s[i] == "(" or s[i] == ")") and (i not in remove)):
            s[i] = ""

    return "".join(s)


print("🚀 ~ file: minRemoveToMakeVaild.py ~ line 21 ~ minRemoveToMakeValid('(a(b(c)d))",
      minRemoveToMakeValid("lee(t(c)o)de)"))
