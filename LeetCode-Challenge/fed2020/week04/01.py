import copy

def findLongestWord(s, d=[]):
    """
    :type s: str
    :type d: List[str]
    :rtype: str
    """

    d.sort()
    tempList = {x:x for x in d}
    maxvalue = 0 
    for c in s:    
        for index in tempList.keys():
            if len(tempList[index]) > 0 and c == tempList[index][0]:
                tempList[index] = tempList[index][1::]
            if tempList[index] == "" and len(index) > maxvalue: 
                maxvalue = len(index)
                
    for key, value in tempList.items():
        if value == "" and len(key) == maxvalue:
            return key
    return ""
    




print(findLongestWord("foobarfoobar", ["foo","bar"]))


    