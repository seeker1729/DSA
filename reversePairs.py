'''
Brute Force Approach : Using two nested Loops
TC : O(n^2) SC: O(1)

Optimized Approach: Using Merge Sort
TC: O(nlogn) SC: O(n)
'''

class Solution:
    def merge(self, left, right, nums):
        nl, nr, n = len(left), len(right), len(nums)
        i, j = 0, 0
        while i < nl and j < nr:
            if left[i] > 2 * right[j]:
                self.count += (nl - i)
                j += 1
            else:
                i += 1
        i, j, k = 0, 0, 0
        while i < nl and j < nr:
            if left[i] > right[j]:
                nums[k] = right[j]
                j += 1
            else:
                nums[k] = left[i]
                i += 1
            k += 1
        while i < nl:
            nums[k] = left[i]
            i += 1
            k += 1
        while j < nr:
            nums[k] = right[j]
            j += 1
            k += 1
        return nums
            
    
    def mergeSort(self, nums):
        if len(nums) == 1:
            return nums
        mid = len(nums) // 2
        leftSub = self.mergeSort(nums[:mid])
        rightSub = self.mergeSort(nums[mid:])
        return self.merge(leftSub, rightSub, nums)
    
    
    def reversePairs(self, nums: list[int]) -> int:
        self.count = 0
        self.mergeSort(nums)
        return self.count


    