# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
            if len(lists) == 0:
                return None
            # 모든 연결리스트들을 순회하면서 숫자들을 가져온 후, 정렬시킨다.
            # 해당 정렬된 숫자를 다시 리스트로 순차적으로 연결한다.
            ans = ListNode();head=ListNode()
            head = ans
            
            arr = []
            for tmp in lists:
                while tmp != None:
                    arr.append(tmp.val)
                    tmp = tmp.next
            arr.sort()
            for n in arr:
                tmp = ListNode(n)
                ans.next = tmp
                ans = ans.next
            
            return head.next
        