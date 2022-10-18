'''
Approach 1:
Use Two Hashsets and once you see the first node common in the LLs, return it
TC : O(n) SC: O(n)

BEST
Approach 2:
TC : O(n) SC : O(1)

'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return None
        # to get rid of offset distance at the beginning
        curA, curB = headA, headB
        while curA and curB:
            curA = curA.next
            curB = curB.next
        
        newA, newB = headA, headB
        # now get rid of the offset so the distance of common node will be same from newA and newB
        while curB:
            newB = newB.next
            curB = curB.next
        
        while curA:
            newA = newA.next
            curA = curA.next
        
        # find the common node if exists
        while newA != newB:
            newA = newA.next
            newB = newB.next
            
        return newA        


