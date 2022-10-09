'''
TC : O(logn) SC : O(1)
'''

class Solution:
    def findPow(self, x, n):
        if n == 0:
            return 1
        temp = self.findPow(x, n // 2)
        if n % 2:
            return (x * temp * temp)
        return (temp * temp)
    
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        exp_neg = False
        if n < 0:
            exp_neg = True
        
        res = self.findPow(x, abs(n))
        if exp_neg:
            return (1 / res)
        return res