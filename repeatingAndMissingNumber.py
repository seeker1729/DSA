'''
Approach 1 :
1. Find freq of all the numbers from 1 to n in array 
2. Element with freq = 0 --> missing Number & freq = 2 --> repeating number
TC -> O(n ^ 2)  SC -> O(1)

Approach 2:
Mapping each number to index and marking their presence (modifies the array)
TC -> O(n)  SC-> O(1)

Approach 3 :
Use the two eqn of sum of first n natural numbers and sum of square of first n natural number
m - r = n * n(n + 1) / 2 - s
m^2 - r^2 = n * (n + 1) * (2n + 1) / 6 - s2
TC -> O(n) SC -> O(1)       
(can have overflow errors)

(BEST)
Approach 4 :
1. calculate xor of all the numbers of array and numbers from 1 to n. We have (m xor r) m^y now
2. get rsb mask of the number 
3. divide the numbers from step 1 into two groups one where this rsb is set other where it is not and take their xor separately
(this will ensure the two numbers we are looking for do not come in the same group and hence can be evaluated)
4. now you have two number one of them is missing other is repeating
5. check from the array which is repeating and missing
TC : O(n)  SC : O(1)
'''


class Solution:
    def repeatedNumber(self, A):
        xor, n = 0, len(A)
        for num in A:
            xor ^= num
        for i in range(1, n + 1):
            xor ^= i
        
        rsb = xor & (-xor)
        first, second = 0, 0
        
        for num in A:
            if num & rsb:
                first ^= num
            else:
                second ^= num
        
        for i in range(1, n + 1):
            if i & rsb:
                first ^= i
            else:
                second ^= i            
        
        for num in A:
            if num == first:
                return first, second
            elif num == second:
                return second, first