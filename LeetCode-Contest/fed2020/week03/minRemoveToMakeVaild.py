def minRemoveToMakeValid(s):
    """
    :type s: str
    :rtype: str
    """

    left = 0
    right = len(s) - 1

    s = [c for c in s]
    remove = []
    while(left <= right):

        if(s[left] == "(" and s[right] == ")"):
            remove.append(left)
            remove.append(right)
            left += 1
            right -= 1
        elif(s[left] != "("):
            left += 1
        elif(s[right] != ")"):
            right -= 1

    for i in range(len(s)):
        if((s[i] == "(" or s[i] == ")") and (i not in remove)):
            s[i] = ""

    return "".join(s)


print("🚀 ~ file: minRemoveToMakeVaild.py ~ line 21 ~ minRemoveToMakeValid('(a(b(c)d)'')",
      minRemoveToMakeValid("))(("))
