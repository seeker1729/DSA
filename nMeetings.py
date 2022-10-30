'''
Approach:
To maximize the number of meetings -> try to host meetings which end early(so we can host as many meetings as 
possible)
-> get an array of pairs (start, end) time of meetings and sort them in ascending order of ending time
TC : O(nlogn) SC : O(n) 
'''

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        meetings = [[start[i], end[i]] for i in range(n)]
        meetings.sort(key = lambda x : (x[1], -x[0]))
        prev, res = float('-inf'), 0
        for s, e in meetings:
            if prev < s:
                res += 1
                prev = e
        return res
        
        
