'''
Approach 1: 
Brute Force : Nested Loops
TC : O(n^2)  SC: O(1)

Approach 2:
Using Hashmap
TC : O(n) SC : O(n)

Approach 3:
Moore's Voting Algorithm
TC : O(n) SC: O(1) 
'''



class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = -1
        freq = 0
        for n in nums:
            if freq == 0:
                candidate = n
                freq = 1
            elif n == candidate:
                freq += 1
            else:
                freq -= 1
                
        return candidate