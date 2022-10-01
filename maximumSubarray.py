'''
Kadane's algorithm

if csum < 0 -> start a new subarray
else : add cur element to existing subarray
'''

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        csum, osum = 0, float('-inf')
        for n in nums:
            if csum < 0:
                csum = n
            else:
                csum += n
            osum = max(osum, csum)
        return osum
        