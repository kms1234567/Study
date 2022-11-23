# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ref = {}
        
        while headA or headB:
            
            if headA:
                if headA in ref:
                    return headA
                else:
                    ref[headA] = True
                    headA = headA.next
            if headB:
                if headB in ref:
                    return headB
                else:
                    ref[headB] = True
                    headB = headB.next
        return None
                