# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ans = ListNode()
        
        dummy = ListNode();dummy = ans
        
        stk = [];cnt = 0
        while head != None:
            stk.append(head.val)
            head = head.next
            cnt += 1
            
            if cnt == k:
                while stk:
                    tmp = ListNode(stk.pop())
                    ans.next = tmp
                    ans = ans.next
                cnt = 0
        for num in stk:
            tmp = ListNode(num)
            ans.next = tmp
            ans = ans.next
        
        return dummy.next
            
            
            