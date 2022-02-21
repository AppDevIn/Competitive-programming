### [171\. Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/)

Difficulty: **Easy**  

Related Topics: [Math](https://leetcode.com/tag/math/), [String](https://leetcode.com/tag/string/)


Given a string `columnTitle` that represents the column title as appear in an Excel sheet, return _its corresponding column number_.

For example:

```
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
```

**Example 1:**

```
Input: columnTitle = "A"
Output: 1
```

**Example 2:**

```
Input: columnTitle = "AB"
Output: 28
```

**Example 3:**

```
Input: columnTitle = "ZY"
Output: 701
```

**Constraints:**

*   `1 <= columnTitle.length <= 7`
*   `columnTitle` consists only of uppercase English letters.
*   `columnTitle` is in the range `["A", "FXSHRXW"]`.


#### Solution

Language: **Python**

```python
class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
​
        total = ord(columnTitle[0]) - 64
        columnTitle = columnTitle[1::]
        for c in columnTitle:
            total = (total * 26) + (ord(c) - 64)
​
        return total
```