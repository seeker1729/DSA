'''
Approach 1:
1. Using a hashset
2. keep adding nodes to the hashset if you reach end (cur == None) => no cycle (return None)
else you will encounter the node that you have already added in the hashset which will be the starting node of the
cycle
TC : O(n) SC : O(n)


Approach 2:
1. check for the cycle using floyd warshall algorithm (slow and fast pointer)
2. Now the distance of starting point of cycle from slow will be same as its distance from head
TC : O(n) SC : O(1)
'''


class Solution:
    def detectCycle(self, head):
        if not head:
            return None
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if fast == None or fast.next == None:
            return None
        
        slow2 = head
        while slow2 != slow:
            slow = slow.next
            slow2 = slow2.next
        return slow
        
        