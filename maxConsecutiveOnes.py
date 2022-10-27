'''
Approach:
1. Traverse the array and if you see a 1 then try to find the longest consecutive subarray with only ones
starting from there
2. else continue
2. compare the current subarray length with overall max
TC : O(n) SC : O(1)
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        maxOnes = 0
        i = 0
        while i < len(nums):
            cur = 0
            while i < len(nums) and nums[i] == 1:
                cur += 1
                i += 1
            maxOnes = max(maxOnes, cur)
            i += 1
        return maxOnes
    
    