'''
Brute Force Approach:
-> Try the recursive approach of all possible combination of coins to get value required
-> And take min of all
TC : exp 

Optimized Approach 1:
-> use the algorithm similar to knapsack
TC : O(V * M) SC : O(V * M)

Optimized Approach 2:
-> improvement over the first approach (slightly different approach)
-> if we observer carefully then we don't need to store the values of all rows (only one row is sufficient and we can keep updating it)
TC : O(V * M) SC : O(V)
'''

# Optimized Approach 1


class Solution:
    def minCoins(self, coins, M, V):
        dp = [[float('inf') for i in range(V + 1)] for j in range(M + 1)]

        # if value required is 0 then 0 coin is required
        for r in range(M + 1):
            dp[r][0] = 0

        res = float('inf')
        for r in range(1, M + 1):
            coin = coins[r - 1]
            for c in range(1, V + 1):
                if c >= coin:
                    #  if the you can use the current coin then compare what will be best
                    #  using the coint or not using the coin
                    dp[r][c] = min(dp[r - 1][c], 1 + dp[r][c - coin])
                else:
                    dp[r][c] = dp[r - 1][c]

        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1

        

# Optimized approach 2
class Solution:
    def minCoins(self, coins, M, V):
        dp = [float('inf')] * (V + 1)
        dp[0] = 0
        for r in range(1, V + 1):
            for c in coins:
                if r - c >= 0:
                    dp[r] = min(dp[r], 1 + dp[r - c])

        return dp[V] if dp[V] != float('inf') else -1
