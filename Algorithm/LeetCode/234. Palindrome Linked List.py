# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        pali = []
        left, right = 0, -1         
        while head != None:
            pali.append(head.val)
            right += 1
            head = head.next
            
        while left <= right:
            if pali[left] != pali[right]:
                return False
            left +=1
            right -= 1
        return True

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        pali = []
        while head != None:
            pali.append(head.val)
            head = head.next
        # 거꾸로 했을 때 같으면 되므로, 뒤집은 후 같은지 확인한다.
        return pali == pali[-1::-1]