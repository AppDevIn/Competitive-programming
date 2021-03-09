# 160. Intersection of Two Linked Lists
# https://leetcode.com/problems/intersection-of-two-linked-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        
        if(not headA or not headB): return None
        
        aStack = [headA]
        bStack = [headB]
        
        while(headA.next or headB.next):            
            if(headA.next != None):
                headA = headA.next
                aStack.append(headA)
                
            if(headB.next != None): 
                headB = headB.next
                bStack.append(headB)
                
        
        
        
        index = -1
        if(aStack[index] != bStack[index]): return None
        while(abs(index) <= min(len(aStack), len(bStack)) and aStack[index] == bStack[index]):
            index -= 1
        
        return aStack[index + 1]
        