'''
Brute Force: 
Four Nested Loops
TC : O(n^4) SC: O(n^)

Optimized Approach:
Using Sorting 
TC : O(n^3) SC: O(n)
'''


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                pairSum = target - nums[i] - nums[j]
                l, r = j + 1, n - 1
                while l < r:
                    if nums[l] + nums[r] == pairSum:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        newl = l
                        while newl < r and nums[newl] == nums[l]:
                            newl += 1
                        l = newl
                    elif nums[l] + nums[r] < pairSum:
                        l += 1
                    else:
                        r -= 1
        return res
    
    