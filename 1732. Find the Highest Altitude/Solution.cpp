class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int iCurAlt = 0;
        int iHighest = 0;
        
        for (const auto &v : gain)
        {
            iCurAlt += v;
            iHighest = iHighest < iCurAlt ? iCurAlt : iHighest;
        }
        
        return iHighest;
    }
};
