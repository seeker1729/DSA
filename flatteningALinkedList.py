'''
Approach 1:
-> Use the merge function of mergesort algorithm to flatten the linked
1. Recursively call to merge the current linked list with the next linked list
2. If the current linked list is empty or there is no next linked list then return the current linked 
list (Base Case)
3. Start merging the linked lists, starting from the last linked list
4. After merging the current linked list with the next linked list, return the head node of the current linked 
list

TC : O(N * N * M) SC : O(N * M) [Auxiliary stack space]  [N & M - no of nodes in the main linked list and sub-
linked list respectively]

Approach 2: (GFG)
Using priority queue
1. Create a priority queue(Min-Heap) and push the head node of every linked list into it
2. While the priority queue is not empty, extract the minimum value node from it and if there is a next node linked to the minimum 
value node then push it into the priority queue
TC : O(N * M * log(N)) SC : O(N)
'''

# Approach 1
class Node:
    def __init__(self, d):
        self.data = d
        self.next = self.bottom = None

def merge(cur, nxt):
    dummy = Node(0)
    temp, temp1, temp2 = dummy, cur, nxt
    while temp1 and temp2:
        if temp1.data <= temp2.data:
            temp.bottom = temp1
            temp1 = temp1.bottom
        else:
            temp.bottom = temp2
            temp2 = temp2.bottom
        temp = temp.bottom
    if temp1:
        temp.bottom = temp1
    else:
        temp.bottom = temp2
    return dummy.bottom

def flatten(root):
    if root == None:
        return None
    nxt = flatten(root.next)
    root.next = None
    return merge(root, nxt)


# Approach 2:
from heapq import heappush, heappop

class Cmp:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.data < other.node.data

def flatten(root):
    pq = []
    while root:
        heappush(pq, Cmp(root))
        root = root.next
    dummy = Node(0)
    temp = dummy
    
    while pq:
        node = heappop(pq).node
        temp.bottom = node
        temp = node
        if node.bottom:
            heappush(pq, Cmp(node.bottom))
    
    return dummy.bottom
    
