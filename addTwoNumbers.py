'''
Approach:
-> Start adding from the last digit (keep track of carry)
-> special cases : Numbers can be of different length
                   after adding all the digits check for the carry
TC : O(max(m, n)) SC : O(max(m, n))
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        newLL = ListNode()
        cur1, cur2, cur = l1, l2, newLL
        carry = 0
        while cur1 and cur2:
            newVal = cur1.val + cur2.val + carry
            carry = newVal // 10
            cur.next = ListNode(newVal % 10)
            cur1 = cur1.next
            cur2 = cur2.next
            cur = cur.next
        
        while cur1:
            newVal = cur1.val + carry
            carry = newVal // 10
            cur.next = ListNode(newVal % 10)
            cur1 = cur1.next
            cur = cur.next
        
        
        while cur2:
            newVal = cur2.val + carry
            carry = newVal // 10
            cur.next = ListNode(newVal % 10)
            cur2 = cur2.next
            cur = cur.next
            
        if carry:
            cur.next = ListNode(1)
            
        return newLL.next
    
    
    