'''
TC : O(n) SC : O(1)
'''
class Solution:
    def rotateRight(self, head, k):
        # base case
        if head == None:
            return None
        #  Get the number of nodes in the list and after counting tail points to last node of list
        count = 1
        tail = head
        while tail.next:
            count += 1
            tail = tail.next
        
        # if k is 0 or multiple of count then simply return the current linked list
        k = k % count
        if k == 0:
            return head
        
        # get the newhead and update the links
        ahead = count - k - 1
        temp2 = head
        
        while ahead:
            ahead -= 1
            temp2 = temp2.next
        
        newhead = temp2.next
        temp2.next = None
        tail.next = head
        return newhead

