'''
-> To calculate how much water will accumulate on any bar we want to know what is the heighest bar to the left
and right of it (include the current bar for finding heighest to the left and right)
water accumulated[i] = min(left, right) - height[i]

Brute Force:
1. for each bar find heighest to left and right and then calculate water accumulated for the current bar
2. do this for every bar
TC : O(n^2) SC : O(1)

Optimized:
1. we can pre-calculate max to left and right using stack and then we can use it directly
TC : O(n) SC : O(n)

BEST:
-> start moving from the two ends 
-> compare the heights at the two ends and then decide which side calculating water accumulated will be
right in the current case and continue
TC : O(n) SC : O(1)
'''

# Brute Force (1)
class Solution:
    def threeSum(self, nums):
        if not nums:
            return []
        n, res = len(nums), []
        nums.sort()
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            pairSum = -1 * nums[i]
            lo, hi = i + 1, n - 1
            
            while lo < hi:
                if nums[lo] + nums[hi] == pairSum:
                    res.append([nums[i], nums[lo], nums[hi]])
                    newlo = lo
                    while newlo < hi and nums[newlo] == nums[lo]:
                        newlo += 1
                    lo = newlo
                elif nums[lo] + nums[hi] < pairSum:
                    lo += 1
                else:
                    hi -= 1
        return res
            

# Optimized (2)  
class Solution:
    def trap(self, height):
        n = len(height)
        maxLeft = [i for i in range(n)]
        stk = []
        for i in range(n):
            while stk and height[stk[-1]] <= height[i]:
                stk.pop()
            if stk:
                maxLeft[i] = stk[-1]
            else:
                stk.append(i)
        stk.clear()
        maxRight = [i for i in range(n)]
        for i in range(n - 1, -1, -1):
            while stk and height[stk[-1]] <= height[i]:
                stk.pop()
            if stk:
                maxRight[i] = stk[-1]
            else:
                stk.append(i)
        
        res = 0
        for i in range(n):
            res += (min(height[maxLeft[i]], height[maxRight[i]]) - height[i])
        
        return res
        
    
# BEST (3)
class Solution:
    def trap(self, height):
        res = 0
        maxLeft, maxRight = 0, 0
        l, r = 0, len(height) - 1
        while l < r:
            # water accumulated depends on min of left and right so calcualte on whichever is smaller
            if height[l] <= height[r]:
                if height[l] >= maxLeft : maxLeft = height[l]
                res += (maxLeft - height[l])
                l += 1
            else:
                if height[r] >= maxRight : maxRight = height[r]
                res += (maxRight - height[r])
                r -= 1
        return res
    
