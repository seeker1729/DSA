'''
Approach:
Since we want all the unique combinations (order of elements in the combination does not matter) so the approach
will be:
-> sort the array first (then all the duplicates will be together (of same value))
-> then at each index either include the value nums[i] in the current combination or skip that value
-> and jump to the next index where the value is not the same
TC : O(2^n)
'''

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        n = len(candidates)
        candidates.sort()
        def dfs(i, comb, csum):
            if csum == target:
                res.append(comb.copy())
                return
            if i == n or csum > target:
                return
            comb.append(candidates[i])
            dfs(i + 1, comb, csum + candidates[i])
            comb.pop()
            while i + 1 < n and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, comb, csum)
        
        dfs(0, [], 0)
        return res
        
        