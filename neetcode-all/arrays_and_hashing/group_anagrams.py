class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #time = o(n * klogk) due to sorting 
        #space = o(n * k) to store strings in dict 
        res = defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))
            res[key].append(s)
        return list(res.values())
