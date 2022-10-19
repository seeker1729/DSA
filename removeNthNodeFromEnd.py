'''
Approach 1: 
1. count number of nodes
2. find the index of node to be removed from the beginning
3. remove the node by traversing the list
TC : O(n) SC : O(1)

Approach 2: (BEST)
-> we can find the nth node from end just by one traversal by using two pointer approach.
-> the n-th node from the end is the same as (total nodes - n)th node from start.
-> move the ahead pointer n times and then move both ahead and behind (start from beginning) together
when ahead reaches end node stop and perform remove operation using behind pointer
TC : O(n) SC : O(1)
'''


class Solution:
    def removeNthFromEnd(self, head, n: int):
        if not head:
            return None
        ahead = head
        while n:
            ahead = ahead.next
            n -= 1
        
        if ahead == None:
            return head.next
        behind = head
        while ahead.next:
            ahead = ahead.next
            behind = behind.next
        
        behind.next = behind.next.next
        return head
