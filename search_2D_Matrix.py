'''
Approach 1 (Brute Force):
Use Linear Search 
TC : O(M * N) SC : O(1)

Approach 2:
1. Start the search from top right corner
2. Move left if value is smaller than target else move down
2. if you find the element return True if move out of bound return False
TC : O(M + N) SC : O(1)

Approach 3:
Use Binary Search (Treat the matrix as a sorted linear array)
k = #columns
matrix to array : matrix[x][y] = arr[k * x + y]
array to matrix : arr[x] = matrix[x//k][x%k]
TC : O(log(M * N)) SC : O(1)
'''
# Approach 2
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        r, c = 0, COLS - 1 
        
        while r < ROWS and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c -= 1
            else:
                r += 1
        
        return False

# Approach 3
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        beg, end = 0, ROWS * COLS - 1
        
        while beg <= end:
            mid = (beg + end) >> 1
            cur = matrix[mid//COLS][mid%COLS]
            if cur == target:
                return True
            elif cur < target:
                beg = mid + 1
            else:
                end = mid - 1
            
        return False