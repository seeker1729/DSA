'''
Approach 1:
1. count the number of nodes
2. find middle node
TC : O(n) SC : O(1)  [Two pass solution]

Approach 2: 
1. Use slow and fast pointer approach to find middle
TC: O(n) SC: O(1) [single pass solution]
'''


class Solution:
    def middleNode(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
    