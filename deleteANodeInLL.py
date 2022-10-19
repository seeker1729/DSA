'''
Approach :
1. traverse the list from current node and start copying the values of next node to cur node upto second last 
node
2. remove the last node
TC : O(n) SC : O(1) 
'''
class Solution:
    def deleteNode(self, node):
        cur = node
        while True:
            cur.val = cur.next.val
            if cur.next.next == None:
                break
            cur = cur.next
        
        cur.next = None
        
        