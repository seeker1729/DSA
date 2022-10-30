'''
Approach:
-> Sort both arrival and departure time arrays
-> Now traverse both the arrays using two pointers and at any time you should have the count of number of 
platforms required (or the number of trains at station) 
-> overall max of the number of trains arriving at the station will give us the number of platforms required
'''

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        arr.sort()
        dep.sort()
        i, j = 0, 0
        curPlatCount = 0
        maxTrainsArrivingSimultaneoulsy = 0
        while i < n and j < n:
            # if prev train has not departed and new train has arrived then one more plat required
            if arr[i] <= dep[j]:
                curPlatCount += 1
                i += 1
            # train departs => one less plat required
            else:
                curPlatCount -= 1
                j += 1
            maxTrainsArrivingSimultaneoulsy = max(maxTrainsArrivingSimultaneoulsy, curPlatCount)
        return maxTrainsArrivingSimultaneoulsy
        
