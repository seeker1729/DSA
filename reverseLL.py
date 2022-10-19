'''
Approach:
Use two pointer approach to reverse the LL (cur and previous pointer)
TC : O(n) SC : O(1)
'''


class Solution:
    def reverseList(self, head):
        cur = head
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        return prev
    
    