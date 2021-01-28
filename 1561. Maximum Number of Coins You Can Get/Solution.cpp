class Solution {
public:
    int maxCoins(vector<int>& piles) {
        int iRet = 0;
        std::sort(piles.begin(), piles.end());
        
        for(int i=0;i<piles.size()/3;i++)
        {
            iRet += piles[piles.size()-2*i-1-1];
        }
        
        return iRet;
    }
};
