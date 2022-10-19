'''
Brute Froce:
Try all subarrays and count the ones with given xor
TC : O(n^2) SC : O(1)

Optimized:
-> Use the concept of prefix xor in the array
-> if the xor upto index i is curXor then for a subarray ending at i whose xor is equal to B
we can write : k^B = curXor
=> k = curXor ^ B
Now how many such values of k exists will give us the number of subarrays ending at i whose value is B
(use hashmap to keep track of this)

TC : O(n) SC: O(n)

'''



class Solution:
    def solve(self, A : list, B : int):
        mp = {0:1}
        curXor = 0
        res = 0
        for n in A:
            curXor ^= n
            res += mp.get(curXor ^ B, 0)
            mp[curXor] = mp.get(curXor, 0) + 1
        return res
        
        