class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> defaultdict;

        for(auto &s: strs){
            string key = s;
            sort(key.begin(), key.end());
            defaultdict[key].push_back(s);
        }
        vector<vector<string>> res;

        for(auto &d:defaultdict){
            res.push_back(d.second);
        }
        return res;
    }
};
