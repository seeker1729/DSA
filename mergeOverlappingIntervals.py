'''
1. Sort the intervals
2. Append if no overlap else merge
'''

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        mergedIntervals = []
        # sort the intervals
        intervals.sort()       
        for start, end in intervals:
            # if overlap merge
            if mergedIntervals and mergedIntervals[-1][1] >= start:
                mergedIntervals[-1][1] = max(mergedIntervals[-1][1], end)
            # else add it to res List
            else:
                mergedIntervals.append([start, end])
                
        return mergedIntervals
        