def minRemoveToMakeValid(s):
    """
    :type s: str
    :rtype: str
    """

    curr = 0
    fast = 0

    s = [c for c in s]
    remove = []
    while(fast < (len(s)) and curr < len(s)):

        if(s[curr] == "(" and s[fast] == ")" and curr < fast):
            remove.append(curr)
            remove.append(fast)
            curr += 1
            fast += 1
        elif(s[curr] != "("):
            curr += 1
        elif(curr > fast):
            fast += 1
        elif(s[fast] != ")"):
            while(fast != len(s) and s[fast] != ")"):
                fast += 1

    for i in range(len(s)):
        if((s[i] == "(" or s[i] == ")") and (i not in remove)):
            s[i] = ""

    return "".join(s)


print("🚀 ~ file: minRemoveToMakeVaild.py ~ line 21 ~ minRemoveToMakeValid('(a(b(c)d)'')",
      minRemoveToMakeValid("(a(b(c)d)"))
