'''
Approach:
Use simple merge approach (as in merge sort algorithm) for merging the two sorted Lists
TC : O(n + m) SC : O(1)
m, n -> #nodes in list1 and list2
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        cur1, cur2 = list1, list2
        cur = dummy
        while cur1 and cur2:
            if cur1.val < cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            cur = cur.next
        if cur1:
            cur.next = cur1
        else:
            cur.next = cur2
        return dummy.next

    