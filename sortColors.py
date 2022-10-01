'''
Three pointer approach  
'''

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        zeros, cur, twos = 0, 0, len(nums) - 1
        while cur <= twos:
            # if cur fall behind zeros update it and check if the cur <= twos
            if cur < zeros:
                cur = zeros
            if cur > twos:
                break
            if nums[cur] == 0:
                nums[cur], nums[zeros] = nums[zeros], nums[cur]
                zeros += 1
            elif nums[cur] == 1:
                cur += 1
            else:
                nums[cur], nums[twos] = nums[twos], nums[cur]
                twos -= 1
                
        # To the left of zeros we have all the 0's
        # To the right of twos we have all the 2's
        # Between zeros and twos we have the all the 1's