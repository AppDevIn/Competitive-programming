def arrayStringsAreEqual(word1: [str], word2: [str]) -> bool:
    
    str1 = ''.join(word1)
    str2 = ''.join(word2)

    word1 = [word for word in str1]
    word2 = [word for word in str2]

    return word1 == word2


print(arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]))
print(arrayStringsAreEqual(["a", "cb"], ["ab", "c"]))