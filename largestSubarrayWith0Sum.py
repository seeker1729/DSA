'''
Brute Force:
Try all the subarrays and find the length of longest with 0 sum
TC : O(n^2)  SC : O(1)

Optimized:
Calculate the sum of elements upto an index and keep adding these to a map (sum : index), index is 
the smallest index upto which the given sum was found. If the sum is already there in map at any time that
means we have found a subarray with 0 sum and we can calculate its length

find the longest subarray with 0 sum
TC : O(n) SC: O(n)
'''
class Solution:
    def maxLen(self, n, arr):
        mp = {0 : -1}
        maxLen = 0
        csum = 0
        for i, num in enumerate(arr):
            csum += num
            if csum in mp:
                maxLen = max(maxLen, i - mp[csum])
            else:
                mp[csum] = i
                
        return maxLen


