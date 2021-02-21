def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """

    romanDictionary = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    multiRomanDictionary = {
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }

    romanValue = 0
    index = 0
    while(index < len(s)):

        if index+1 < len(s) and s[index] in ["I", "X", "C"] and (s[index] + s[index+1]) in multiRomanDictionary.keys():
            romanValue += multiRomanDictionary[s[index] + s[index+1]]
            index += 1
        else:
            romanValue += romanDictionary[s[index]]
        index += 1
    return romanValue





print("🚀 ~ file: romanToInteger.py ~ line 25 ~ romanToInt", romanToInt("MCMXCIV"))

    