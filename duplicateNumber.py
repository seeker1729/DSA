'''
Brute Force Approach :
1. Use two nested loops to find repeating Number
TC -> O(n ^ 2) SC -> O(1)

(BETTER) HashMap Approach :
1. Get frequency map of elements in the array
2. repeating number == element with freq > 1
TC -> O(n) SC -> O(n)

(BEST 1 (Array modified)) :
Length of array -> n + 1   values in Range [1, n]
--> Each value can be mapped to an index in the array 
1. Mark the presence if each number i at index i by making nums[i] -ve
2. if the value already -ve => repeating number (i)
TC -> O(n) SC -> O(1) 

***BEST 2 (Floyd warshall Cycle Detection Algorithm) :
--> Think of the array as a linked list 
--> Since there is repeating number LL will contain cycle 
--> the starting node of cycle will be the repeating number
--> start with node with value 0 (cannot be the repeating number since not in given range)

e.g -> [3,1,3,4,2]
LL ->  0 -> 3 -> 4 -> 2 -> "3"

'''

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # initially slow fast point to 0
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                # cycle detected 
                break
        
        # distance of slow from starting point of cycle = distance of starting point of cycle from starting of LL
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
        return slow