'''
Approach :
-> reverse one group at a time and then recursively call for remaining LL
TC : O(n) SC : O(1)

-> By writing the same approach in iterative way
TC : O(n) SC : O(1)
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Recursive solution 
class Solution:
    def reverseKGroup(self, head, k):
        # Base cases
        if head == None:
            return None
        cnt, cur = 0, head
        while cur and cnt < k:
            cur = cur.next
            cnt += 1
        if cnt < k:
            return head

        # reverse k nodes
        cur2 = head
        prev = None
        while cnt:
            nxt = cur2.next
            cur2.next = prev
            prev = cur2
            cur2 = nxt
            cnt -= 1
        # recursively call for remaining LL 
        head.next = self.reverseKGroup(cur, k)
        return prev


#Iterative solution
class Solution:
    def reverseKGroup(self, head, k: int):
        # calculate the number of groups in the LL
        cur = head
        cntNodes = 0
        while cur:
            cur = cur.next
            cntNodes += 1
        groups = cntNodes // k
        if groups == 0:
            return head
        
        # dummy node to gather nodes of modified LL
        dummy = ListNode()
        temp = dummy
        cur = head
        groupsLeft = groups
        # reverse the groups and make next of prev group end point to current groups head
        while cur and groupsLeft:
            cnt = k
            prev = None
            newTemp = cur
            while cnt:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
                cnt -= 1
            temp.next = prev
            temp = newTemp
            groupsLeft -= 1
        
        temp.next = cur
        return dummy.next
        
        
        
        