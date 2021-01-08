def lengthOfLongestSubstring(s: str) -> int: 
    l =  [x for x in s]
    sl = list(set(l))

    if len(sl) == 1:
        return len(sl)

    nL = [[]]
    for x in range(0, len(l)):
        curr = nL[len(nL)-1]
        

        if l[x] not in curr :
            curr.append(l[x])
        else:
            nL[len(nL)-1] = curr
            nL.append([l[x]])
            if l[x-1] not in nL[len(nL)-1] :
                nL[len(nL)-1].append(l[x-1])


    return max([len(x) for x in nL ])


    


            

    



print(lengthOfLongestSubstring(""))
print(lengthOfLongestSubstring("dvdf"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring("abcabcbb"))