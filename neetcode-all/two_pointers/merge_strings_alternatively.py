class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #O(n) time and O(n) space 
        res = []
        l, r = 0, 0 

        while l < len(word1) and r < len(word2):
            res.append(word1[l])
            res.append(word2[r])
            l += 1
            r += 1
        
        if word1:
            res.append(word1[l:])
        if word2:
            res.append(word2[r:])
        
        return ''.join(res)
        
         

