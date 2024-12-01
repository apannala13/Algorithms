class Solution:
    def validPalindrome(self, s: str) -> bool:
        #O(n) time, O(n) space due to slicing of substrings
        def is_palindrome(sub):
            return sub == sub[::-1]
        
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                return True if is_palindrome(s[l:r]) or is_palindrome(s[l+1:r + 1]) else False
            l += 1
            r -= 1
        return True 
    
