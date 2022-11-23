# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 솔루션
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next

# 내가 푼 것
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1_list = [];l2_list=[]
        # while 문으로 연결리스트를 돌면서 각 값들을 저장함 
        while(True):
            l1_list.append(str(l1.val))
            if (l1.next):
                l1 = l1.next
            else:
                break
        while(True):
            l2_list.append(str(l2.val))
            if (l2.next):
                l2 = l2.next
            else:
                break
        
        # reversed 시켜서 반대로 저장함
        l1_str = ''.join(str(s) for s in reversed(l1_list))
        l2_str = ''.join(str(s) for s in reversed(l2_list))

        # int형으로 변경하면서 더하고, 길이를 알아냄
        res = int(l1_str) + int(l2_str)
        len_res = len(str(res))-1

        ans = []
        
        # 알아낸 길이로 10**i 으로 나눈 값을 저장
        for i in range(len_res, -1, -1):
            ans.append(ListNode(res//10**i, None))
            res = res % (10**i)
        
        # 다시 리버스시켜서 연결
        ans.reverse()
        ret = ans[0]
        for i in range(0,len(ans)-1):
            ans[i].next = ans[i+1]

        return ret
        
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        