class Solution:
    def isPalindrome(self, s: str) -> bool:
        #O(n) time, O(1) space 
        s = s.lower()
        l, r = 0, len(s) - 1
        
        for i in range(len(s)):
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                if not s[l] == s[r]:
                    return False
                else:
                    l += 1
                    r -= 1
        return True 
