'''
Floyd's cycle detecting algorithm
TC : O(n) SC: O(1)
'''

class Solution:
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False
    
    