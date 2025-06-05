# [1061. Lexicographically Smallest Equivalent String](https://leetcode.com/problems/lexicographically-smallest-equivalent-string/description/?envType=daily-question&envId=2025-06-05)

You are given two strings of the same length <code>s1</code> and <code>s2</code> and a string <code>baseStr</code>.

We say <code>s1[i]</code> and <code>s2[i]</code> are equivalent characters.

- For example, if <code>s1 = "abc"</code> and <code>s2 = "cde"</code>, then we have <code>'a' == 'c'</code>, <code>'b' == 'd'</code>, and <code>'c' == 'e'</code>.

Equivalent characters follow the usual rules of any equivalence relation:

- **Reflexivity:**  <code>'a' == 'a'</code>.
- **Symmetry:**  <code>'a' == 'b'</code> implies <code>'b' == 'a'</code>.
- **Transitivity:**  <code>'a' == 'b'</code> and <code>'b' == 'c'</code> implies <code>'a' == 'c'</code>.

For example, given the equivalency information from <code>s1 = "abc"</code> and <code>s2 = "cde"</code>, <code>"acd"</code> and <code>"aab"</code> are equivalent strings of <code>baseStr = "eed"</code>, and <code>"aab"</code> is the lexicographically smallest equivalent string of <code>baseStr</code>.

Return the lexicographically smallest equivalent string of <code>baseStr</code> by using the equivalency information from <code>s1</code> and <code>s2</code>.

**Example 1:** 

```
Input: s1 = "parker", s2 = "morris", baseStr = "parser"
Output: "makkek"
Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [m,p], [a,o], [k,r,s], [e,i].
The characters in each group are equivalent and sorted in lexicographical order.
So the answer is "makkek".
```

**Example 2:** 

```
Input: s1 = "hello", s2 = "world", baseStr = "hold"
Output: "hdld"
Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [h,w], [d,e,o], [l,r].
So only the second letter 'o' in baseStr is changed to 'd', the answer is "hdld".
```

**Example 3:** 

```
Input: s1 = "leetcode", s2 = "programs", baseStr = "sourcecode"
Output: "aauaaaaada"
Explanation: We group the equivalent characters in s1 and s2 as [a,o,e,r,s,c], [l,p], [g,t] and [d,m], thus all letters in baseStr except 'u' and 'd' are transformed to 'a', the answer is "aauaaaaada".
```

**Constraints:** 

- <code>1 <= s1.length, s2.length, baseStr <= 1000</code>
- <code>s1.length == s2.length</code>
- <code>s1</code>, <code>s2</code>, and <code>baseStr</code> consist of lowercase English letters.
