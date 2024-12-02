class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        #O(n + m)
        return True if ''.join(word1) == ''.join(word2) else False
        
