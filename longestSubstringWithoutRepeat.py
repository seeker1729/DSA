'''
Brute Force:
Try each substring and find the longest one without repeating characters
TC : O(n^2) SC : O(n)

Optimized:
-> Use sliding window to keep track of the cur Substring without repeating character
-> Use a hashset to check for repeating character
-> when you see a repeating character start moving the starting point of window until you get rid of previous 
occurence of that character and continue
-> keep updating the res value if it needs to be
TC : O(n) SC : O(n)

'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        res, charSet = 0, set()
        while end < len(s):
            while s[end] in charSet:
                charSet.remove(s[start])
                start += 1
            charSet.add(s[end])
            end += 1
            res = max(res, len(charSet))
            
        return res
    
    