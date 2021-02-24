def lengthOfLongestSubstring(s: str) -> int: 
    l =  [x for x in s]
    sl = list(set(l))

    if len(sl) == 1 or len(sl) == 0:
        return len(sl)

    nL = []
    curr = []
    for x in range(0,len(l)-1):
        nL.append(curr)
        curr = []
        for j in range(x,len(l)):
            if l[j] not in curr:
                curr.append(s[j])
            else:
                break
        nL.append(curr)
        
    return max([len(x) for x in nL])            


    


            

    



print(lengthOfLongestSubstring(""))#0
print(lengthOfLongestSubstring("au"))#2
print(lengthOfLongestSubstring("dvdf"))#3
print(lengthOfLongestSubstring("bbbbb"))#1
print(lengthOfLongestSubstring("pwwkew"))#3
print(lengthOfLongestSubstring("abcabcbb")) #3
print(lengthOfLongestSubstring("anviaj")) #5