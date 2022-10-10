# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        # 전, 현, 후 노드들을 이용하여 관계를 수정합니다.
        prev, cur, nxt = None, head, head.next
        
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            
        return prev