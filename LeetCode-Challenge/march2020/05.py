# 637. Average of Levels in Binary Tree
# https://leetcode.com/problems/average-of-levels-in-binary-tree/solution/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    dictory = {}
    
    def recur(self, root: TreeNode, level: int):
        
   
        
        if level in self.dictory.keys():
            self.dictory[level].append(root.val)
        else:self.dictory[level] = [root.val]
        
        if root.left == None and root.right == None:
            return
        
        if root.left is not None:
            self.recur(root=root.left, level=level+1)
        if root.right is not None:
            self.recur(root=root.right, level=level+1)
            
            
        
        
        
        
    def averageOfLevels(self, root: TreeNode):
        self.recur(root, 0)
        
        results = []
        for x in self.dictory.keys():
            results.append(sum(self.dictory[x])/len(self.dictory[x]))
            
        
        return results
s = Solution()

s.averageOfLevels(TreeNode(5, TreeNode(2), TreeNode(-3)))
        