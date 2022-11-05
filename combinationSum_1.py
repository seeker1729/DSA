'''
Approach:
-> Two choices at each index
    => take the element and stay at that index
    => donot take the cur element and move to next index
TC : O(2^n) SC : O(n^2) 
'''

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        def combSum(i, csum, curComb):
            if csum == target:
                res.append(curComb.copy())
                return 
            if i == len(candidates) or csum > target:
                return 
            curComb.append(candidates[i])
            combSum(i, csum + candidates[i], curComb)
            curComb.pop()
            combSum(i + 1, csum, curComb)
        combSum(0, 0, [])
        return res
    
    