Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        answer = [[root.val]]
        queue = [[root]]
        curr = queue[0]
        tmp = []
        
        while answer[-1] != []:
            vals = []
            for node in curr:
                if node.left:
                    tmp.append(node.left)
                    vals.append(node.left.val)

                if node.right:    
                    tmp.append(node.right)
                    vals.append(node.right.val)
        
                    
            queue.append(tmp)
            answer.append(vals)
            curr = tmp
            tmp = []
        return answer[0:-1]
            
        
            
        
