class Solution:
    def reverseWords(self, s: str) -> str:
        #O(N) space solution: return ' '.join(x[::-1] for x in s.split())

        #two ptr, still o(n) space 
        l, r = 0, 0
        res = ''

        while r < len(s):
            if s[r] != ' ':
                r += 1
            else:
                res += s[l:r][::-1] + ' '
                r += 1
                l = r
        
        res += s[l:r][::-1]
        return res
