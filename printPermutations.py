'''
Approach:
-> get all possible permutations using brute force
TC : O(n * n!) SC: O(n^2)
'''

class Solution:
    def getAllPermutations(self, nums, res, cur):
        if len(nums) == 0:
            return res.append(cur.copy())
        for i in range(len(nums)):
            cur.append(nums[i])
            self.getAllPermutations(nums[:i] + nums[i + 1:], res, cur)
            cur.pop()
    
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        self.getAllPermutations(nums, res, [])
        return res
    
    