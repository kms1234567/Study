# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        existence = set()
        
        tmp = None
        while head != None:
            if head in existence:
                tmp = head
                break
            
            existence.add(head)            
            head = head.next
        return tmp