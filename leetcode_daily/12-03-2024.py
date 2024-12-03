class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        # prev = 0

        # for index in spaces:
        #     res.append(s[prev:index])
        #     prev = index
        
        # res.append(s[prev:])
        # return ' '.join(res)

        l = 0
        for i, n in enumerate(s):
            if l < len(spaces) and i == spaces[l]:
                res.append(' ')
                l += 1
            res.append(n)
        return ''.join(res)



