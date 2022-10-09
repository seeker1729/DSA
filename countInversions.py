'''
Brute Force Approach:
Consider all the pairs and then count the inversion pairs
TC : O(n ^ 2)  SC : O(1)

Using MergeSort: TC : O(nlogn) SC : O(n)
'''
class Solution:    
    def merge(self, left, right, arr):
        nl, nr, n = len(left), len(right), len(arr)
        i, j, k = 0, 0, 0
        while i < nl and j < nr:
            if left[i] > right[j]:
                self.count += (nl - i)
                arr[k] = right[j]
                j += 1
            else:
                arr[k] = left[i]
                i += 1
            k += 1
        
        while i < nl:
            arr[k] = left[i]
            i += 1
            k += 1
        while j < nr:
            arr[k] = right[j]
            j += 1
            k += 1
        return arr
    
    def mergeSort(self, arr):
        if len(arr) == 1:
            return arr
        mid = len(arr) // 2
        leftSub = self.mergeSort(arr[:mid])
        rightSub = self.mergeSort(arr[mid:])
        return self.merge(leftSub, rightSub, arr)
        
    
    def getInversions(self, arr, n):
        self.count = 0
        self.mergeSort(arr)
        return self.count
