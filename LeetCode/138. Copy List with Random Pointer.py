class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        cur = head 
        # hashmap for maintaining old node
        oldNode = { None : None }
        # 딕셔너리에 해당 인스턴스를 key로 새로 생성한 copy 인스턴스를 vlaue로 저장한다.
        while cur :
            copy = Node(cur.val)
            oldNode[cur] = copy 
            cur = cur.next
        cur = head
        # 새로 생성한 인스턴스에 접근해 모두 대체한다.
        while cur :
            copy = oldNode[cur]
            copy.random=oldNode[cur.random]
            copy.next=oldNode[cur.next]
            cur = cur.next
           
        return oldNode[head] 
            
        