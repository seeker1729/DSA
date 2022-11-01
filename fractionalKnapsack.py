'''
Approach:
=> Sort the items based on (val / weight), since we are allowed to break the items we will pick the items which
more value of this ratio
=> just keep on adding till we have cap left and we will get the max value
TC : O(NlogN) SC : O(1)
'''

class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,Items,n):
        Items.sort(key = lambda item : (item.value / item.weight), reverse = True)
        maxValue = 0
        capacityLeft = W
        for item in Items:
            val, wt = item.value, item.weight
            if capacityLeft > wt:
                maxValue += val
                capacityLeft -= wt
            else:
                maxValue += (capacityLeft * (val / wt))
                capacityLeft = 0
                break
        return maxValue
        
