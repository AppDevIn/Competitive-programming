### [104\. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

Difficulty: **Easy**  

Related Topics: [Tree](https://leetcode.com/tag/tree/), [Depth-First Search](https://leetcode.com/tag/depth-first-search/), [Breadth-First Search](https://leetcode.com/tag/breadth-first-search/), [Binary Tree](https://leetcode.com/tag/binary-tree/)


Given the `root` of a binary tree, return _its maximum depth_.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg)

```
Input: root = [3,9,20,null,null,15,7]
Output: 3
```

**Example 2:**

```
Input: root = [1,null,2]
Output: 2
```

**Constraints:**

*   The number of nodes in the tree is in the range `[0, 10<sup>4</sup>]`.
*   `-100 <= Node.val <= 100`


#### Solution

Language: **Python3**

```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.rcur(root, 1) if root is not None else 0
​
    def rcur(self, node: TreeNode, depth: int) -> int:
        right_depth, left_depth = depth, depth
        if node.left:
            left_depth = self.rcur(node.left, depth+1)
        if node.right:
            right_depth = self.rcur(node.right, depth+1)
​
        if right_depth > left_depth:
            return right_depth
        else:
            return left_depth
​
​
```