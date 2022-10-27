'''
Approach:
-> all the elements at and to the left will be the unique elements in array
-> left will be pointing to last written unique element (new value will be written at [left + 1] index)
-> if element already written then continue else write the element at index [left + 1] and increment left
-> return (left + 1)
TC : O(n) SC : O(1) 
'''

class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return nums
        left = -1
        for i in range(len(nums)):
            if left == -1 or nums[left] != nums[i]:
                nums[left + 1] = nums[i]
                left += 1
                
        return (left + 1)
        
        