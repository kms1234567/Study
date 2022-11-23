from collections import defaultdict
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
연결리스트를 딕셔너리에 key값으로 해당 value값을 value값은 해당 연결리스트의 인스턴스를 담았다.
그리고, 해당 key값을 sorted 한 후, 해당 연결리스트의 연결관계를 수정하는 방식으로 구현하였다.
"""
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        order_dict = defaultdict(list)
        
        while head != None:
            order_dict[head.val].append(head)
            head = head.next
        
        dummy = None
        head2 = dummy
        prev = None
        for key in sorted(order_dict.keys()):
            for node in order_dict[key]:
                if prev:
                    prev.next = node
                else:
                    head2 = node
                dummy = node
                prev = dummy
                dummy.next = None
                 
        return head2
                