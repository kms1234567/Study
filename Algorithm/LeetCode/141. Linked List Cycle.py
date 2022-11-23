# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # existence에 해당 노드의 인스턴스를 넣고, 이미 존재하면 True, None을 만나 끝나게 되면 False를 반환한다.
        existence = set()
        while head != None:
            if head in existence:
                return True
            existence.add(head)
            head = head.next
        
        return False