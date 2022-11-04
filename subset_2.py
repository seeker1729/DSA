'''
Approach:
-> Use a backtracking option where we will try to get all the possible unique subsets (after sorting the array)
-> Two cases
    => Ist where you include the current element
    => second where you take the next different element

TC : O(n* (2 ^ n)) SC : O(n * (2 ^ n))
'''


class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        def backTrack(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            # include nums[i] in the subset
            backTrack(i + 1, subset)
            subset.pop()

            # don't include nums[i] in the res of subsets to avoid duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backTrack(i + 1, subset)
        backTrack(0, [])
        return res

