'''
Approach 1 -> 
1. declare a temp Matrix of same size as given matrix and with same elements
2. Make all the rows and columns zero in temp matrix where the cell in original matrix has 0
3. copy elements of temp into original

TC -> O(m * n * (m + n)) SC -> O(m * n)

Approach 2 -> 
1. get a row and col set which need to be made zero by traversing the matrix
2. make all the rows and columns of set 0
TC -> O(m * n)  SC -> O(m + n)


(BEST) Approach 3 ->
--> store the info about which row and column need to be made zero in the matrix itself
--> Use col 0 for storing info about rows and row 0 for storing info about columns 
--> Go through the matrix if matrix[r][c] == 0 then make matrix[0][c] = 0 (marked the column) and matrix[r][0] = 0 (marked the row)
--> ** matrix[0][0] is being used for two info row 0 as well as col0 so we will use a variable row0 for storing info about row 0

TC -> O(m * n)  SC -> O(1)
'''
# BEST 
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        row0 = False  # variable for row 0
        for r in range(ROWS):
            for c in  range(COLS):
                # mark the rows and column to be made 0
                if matrix[r][c] == 0:
                    if r == 0:
                        row0 = True
                    else:
                        matrix[r][0] = 0
                    matrix[0][c] = 0
        
        # without modifying the first row and column change the rest of elements if they need to be
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # first check for col 0 then row0 else it can lead to errors 
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
                
        if row0:
            for c in range(COLS):
                matrix[0][c] = 0
                
                
        
