#  function calculates the number of stable states for current window
def calculateStates(length):
    count = 0
    # possible stable states starting with first elemet (cur)
    cur = length - 2
    while cur:
        count += cur
        cur -= 1
    return count


def solution(A):
    # If the number of elements less than 3 -> no stable state
    if len(A) < 3:
        return 0
    res = 0
    # initial conditions 
    start, end = 0, 2
    diff = A[1] - A[0]
    cur = 1

    while cur < len(A):
        # if end within bound and next element can be included in the window then include it
        if end < len(A) and A[end] - A[cur] == diff:
            end += 1
            cur += 1
        # otherwise process the current window and move to next one
        else:
            # find cur window length and find number of possible stable states in that
            curWindowLength = end - start 
            if curWindowLength >= 3:
                res += calculateStates(curWindowLength)
            # update the pointers to move to the next possible window
            start = cur
            if end < len(A) : diff = A[end] - A[cur]
            cur += 1
            end += 1
    
    return res if res <  10 ** 9 else -1


print(solution([-1, 1, 3, 3, 3, 2, 3, 2, 1, 0]))
print(solution([7, 6, 5, 4, 3, 2]))


