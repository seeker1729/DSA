'''
Brute Force Approach : Using Two Nested Loops
TC : O(n^2) SC: O(1)

Using Hashmap:
TC : O(n) SC: O(n) 
'''


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mp = {}
        for i, num in enumerate(nums):
            mp[num] = i
            
        for i, num in enumerate(nums):
            if target - num in mp and mp[target - num] != i:
                return [i, mp[target - num]]
        return [-1, -1]
    
    