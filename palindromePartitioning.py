'''
Backtracking:
At each index consider all the palindromic partitions possible from there and continue from there
TC : O(n * (n ^ 2)) SC : O(n^2)
'''

class Solution:
    def checkPali(self, s, i, j):
        l, r = i, j
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    
    def partition(self, s: str) -> list[list[str]]:
        res = []
        def dfs(i, part):
            if i == len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.checkPali(s, i, j):
                    part.append(s[i:j + 1])
                    dfs(j + 1, part)
                    part.pop()
                    
        dfs(0, [])
        return res
            
        