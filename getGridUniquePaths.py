
# Recursion with memoization 
# TC : O(m*n) SC: O(m*n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]
        def dfs(r, c):
            if r == m - 1 and c == n - 1:
                return 1
            elif r > m - 1 or c > n - 1:
                return 0
            if dp[r][c] != -1:
                return dp[r][c]
            countPaths = 0
            countPaths += dfs(r + 1, c)
            countPaths += dfs(r, c + 1)
            dp[r][c] = countPaths
            return countPaths
        return dfs(0, 0)

# Tabulation Solution
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if r == m - 1 and c == n - 1:
                    dp[r][c] = 1
                else:
                    dp[r][c] = dp[r + 1][c] + dp[r][c + 1]
                    
        return dp[0][0]

# Tabulation Solution Space Optimized
# SC: O(n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [0 for i in range(n + 1)]
        for r in range(m - 1, -1, -1):
            cur = [0 for i in range(n + 1)]
            for c in range(n - 1, -1, -1):
                if r == m - 1 and c == n - 1:
                    cur[c] = 1
                else:
                    cur[c] = cur[c + 1] + prev[c]
            prev = cur
        return cur[0]


'''
Math Solution
This is a combinatorial problem and can be solved without DP. For mxn grid, robot has to move exactly m-1 steps down and n-1 steps right and these can be done in any order.
m = 3, n = 7, ans = 28
For the eg., given in question, 3x7 matrix, robot needs to take 2+6 = 8 steps with 2 down and 6 right in any order. That is nothing but a permutation problem. Denote down as 'D' and right as 'R', following is one of the path :-

D R R R D R R R

We have to tell the total number of permutations of the above given word. So, decrease both m & n by 1 and apply following formula:-
Total permutations = (m + n - 2)! / ((m - 1)! * (n - 1)!)
'''

from math import factorial
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        possible_ways = factorial(m + n - 2) / (factorial(m - 1) * factorial(n - 1))
        return int(possible_ways)
    
    