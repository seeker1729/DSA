'''
Approach 1:
-> Using HashMap
1. First map all the nodes of the original linked list to their copies
2. Then in the next traversal update the pointers
TC : O(N) SC : O(N)

Approach 2:
-> sandwich the copied nodes in the original list
-> now we can easily update and track the random pointers for copied list
TC : O(N) SC : O(1)
'''

class Node:
    def __init__(self, x, next, random):
        self.val = x
        self.next = next
        self.random = random

#  Approach 1
class Solution:
    def copyRandomList(self, head):
        if head == None:
            return None
        #  Map Node : NodeCopy
        copyMp = {}
        temp = head
        while temp:
            tempCopy = Node(temp.val)
            copyMp[temp] = tempCopy
            temp = temp.next
        temp = head
        while temp:
            # for next pointer
            if temp.next : copyMp[temp].next = copyMp[temp.next]
            # for random pointer
            if temp.random : copyMp[temp].random = copyMp[temp.random]
            temp = temp.next
        
        return copyMp[head]
        
        
# Approach 2
class Solution:
    def copyRandomList(self, head):
        if head == None:
            return None
        
        # sandwich the copied nodes in the original list        
        temp = head
        while temp:
            nxt = temp.next
            copy = Node(temp.val)
            temp.next = copy
            copy.next = nxt
            temp = nxt
        
        # update random pointers for copied nodes
        temp = head
        while temp:
            nxt = temp.next.next
            copy = temp.next
            if temp.random : copy.random = temp.random.next
            temp = nxt
        
        # restore the original linked list
        dummy = Node(0)
        temp, tempCopy = head, dummy
        while temp:
            nxt = temp.next.next
            copy = temp.next
            tempCopy.next = copy
            tempCopy = copy
            temp.next = nxt
            temp = nxt
        
        
        return dummy.next
        