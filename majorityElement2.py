'''
Brute Force Approach : Nested Loops
TC : O(n^2) SC : O(1)

Using Hashmap:
TC : O(n) SC: O(n)

Moore's Voting Algorithm:
For the general problem, looking for elements appearing more than ⌊N/k⌋ times for some positive integer k, there can be atmost k - 1 such 
Elements
https://leetcode.com/problems/majority-element-ii/discuss/63502/6-lines-general-case-O(N)-time-and-O(k)-space
TC : O(n * k) SC : O(k)
'''


from collections import Counter
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        ctr = Counter()
        for n in nums:
            ctr[n] += 1
            if len(ctr) == 3:
                ctr -= Counter(set(ctr))
        
        return [n for n in ctr if nums.count(n) > (len(nums) // 3)]
    
    
    