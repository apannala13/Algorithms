class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int total = 0;
        int l = 0;

        for(int r = 0; r < prices.size(); ++r){
            if(prices[r] > prices[l]){
                int current = prices[r] - prices[l];
                total += current;
            }
            l = r;
        }
        return total;
        
    }
};
