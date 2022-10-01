'''
logic -> to get next greater permutation in lexicographical order we want to change values on as right 
as possible (because that will give us smallest change in magnitude and just greater permutation)


Algo:
1. start from the right of array and look for first index (if there) where nums[i] < nums[i + 1]
    i) start traversing from right and first index j where nums[j] > nums[i] : (swap(nums[i], nums[j]))
    ii) break
2. reverse nums from i + 1 to end


e.g. -> [2, 3, 1]

    i
1. [2, 3, 1]
        i  j            i
    i) [2, 3, 1] -> [3, 2, 1]

2. [3, 1, 2] -> res
'''
class Solution:  
    def reverse(self, nums, lo, hi):
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo += 1
            hi -= 1
    
    def nextPermutation(self, nums: list[int]) -> None:
        i = len(nums) - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                j = len(nums) - 1
                while nums[j] <= nums[i]:
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]
                break
            i -= 1
        self.reverse(nums, i + 1, len(nums) - 1)