'''
Approach:
Find the starting number of permutation using basic maths and keep calling the function to find the remaining numbers of the sequence
'''

from math import factorial
from sortedcontainers import SortedSet, SortedList, SortedDict
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # with a given set of numbers function find the cnt th permutation
        def permutation(numb, cnt):
            # base case
            if cnt == 1:
                res = ''
                for n in numb:
                    res += str(n)
                return res
            cnt_numb = len(numb)
            # starting with any number in the given set cnt_perm permutation will be possible
            cnt_perm = factorial(cnt_numb - 1)
            perm = 0
            for n in numb:
                perm += cnt_perm
                if perm >= cnt:
                    cur = n
                    break
            numb.remove(cur)
            res = (str(cur) + permutation(numb, cnt + cnt_perm - perm))
            return res
        res = permutation(SortedSet([i for i in range(1, n + 1)]), k)
        return 
    
    
    