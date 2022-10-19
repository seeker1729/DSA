'''
Approach 1:
-> create an array of nodes values and check if it is a palindrome
TC : O(n) SC : O(n)

Approach 2:
-> we can solve this in single traversal without using extra space
-> reverse the starting mid portion of LL
-> start comparing the values as you move away from mid

e.g 
1 -> 2 -> 2 -> 1
<- 1 <- 2 2-> 1
1 -> 2 -> 2 -> 1
TC : O(n) SC : O(1)
'''

# Approach 1
class Solution:
    def isPalindrome(self, head) -> bool:
        listNode = []
        cur = head
        while cur:
            listNode.append(cur.val)
            cur = cur.next
        
        l, r = 0, len(listNode) - 1
        while l < r:
            if listNode[l] != listNode[r]:
                return False
            l += 1
            r -= 1
        return True
        

# Approach 2
class Solution:
    def isPalindrome(self, head) -> bool:
        if head == None or head.next == None:
            return True
        slow, fast, prev = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow  = nxt
        
        if fast == None:
            slow2 = slow
        else:
            slow2 = slow.next
        slow, prev = prev, slow
        
        while slow and slow2:
            if slow.val != slow2.val:
                return False
            slow2 = slow2.next
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        return True
        