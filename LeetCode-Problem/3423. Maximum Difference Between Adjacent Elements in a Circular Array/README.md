# [3423. Maximum Difference Between Adjacent Elements in a Circular Array](https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/description/?envType=daily-question&envId=2025-06-12)

Given a **circular**  array <code>nums</code>, find the <b>maximum</b> absolute difference between adjacent elements.

**Note** : In a circular array, the first and last elements are adjacent.

**Example 1:** 

<div class="example-block">
Input: nums = [1,2,4]

Output: 3

Explanation:

Because <code>nums</code> is circular, <code>nums[0]</code> and <code>nums[2]</code> are adjacent. They have the maximum absolute difference of <code>|4 - 1| = 3</code>.

**Example 2:** 

<div class="example-block">
Input: nums = [-5,-10,-5]

Output: 5

Explanation:

The adjacent elements <code>nums[0]</code> and <code>nums[1]</code> have the maximum absolute difference of <code>|-5 - (-10)| = 5</code>.

**Constraints:** 

- <code>2 <= nums.length <= 100</code>
- <code>-100 <= nums[i] <= 100</code>
