
'''
Approach 1: 
1. Sort the array (first get the array with unique elements)
2. Traverse the array and find longest consecutive sequence
TC: O(nlogn)  SC: O(n)

Approach 2:
First turn the input into a set of numbers. That takes O(n) and then we can ask in O(1) whether we have a certain number.

Then go through the numbers. If the number x is the start of a streak (i.e., x-1 is not in the set), then test y = x+1, x+2, x+3, ... and
stop at the first number y not in the set.The length of the streak is then simply y-x and we update our global best with that.
Since we check each streak only once, this is overall O(n). This ran in 44 ms on the OJ, one of the fastest Python submissions.
'''
# Approach 1
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()        
        curLen, maxLen = 1, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                curLen += 1
            else:
                curLen = 1
            maxLen = max(maxLen, curLen)
            
        return maxLen
    
#Approach 2  
class Solution:
    def longestConsecutive(self, nums):
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best

    