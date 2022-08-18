# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
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
        