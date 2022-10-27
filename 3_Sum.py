'''
Brute Force:
1. Sort the array
2. Use three nested loops to get all triplets with 0 sum and add them to hashset(to get all unique ones)
TC : O(n^3) SC : O(n)

Optimized:
1. Sort the array
2. pick the first element in the outer loop and look for the required pairsum in remaining elements to get the
unique triplets
TC : O(n^2) SC : O(n)
'''
class Solution:
    def threeSum(self, nums):
        if not nums:
            return []
        n, res = len(nums), []
        nums.sort()
        
        for i in range(n - 2):
            # if cur and prev element same -> then continue
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            pairSum = -1 * nums[i]
            lo, hi = i + 1, n - 1
            
            while lo < hi:
                if nums[lo] + nums[hi] == pairSum:
                    res.append([nums[i], nums[lo], nums[hi]])
                    newlo = lo
                    # to avoid having duplicate triplets
                    while newlo < hi and nums[newlo] == nums[lo]:
                        newlo += 1
                    lo = newlo
                elif nums[lo] + nums[hi] < pairSum:
                    lo += 1
                else:
                    hi -= 1
        return res
            
        