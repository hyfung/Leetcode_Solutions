class Solution {
public:
    vector<bool> checkArithmeticSubarrays(vector<int>& nums, vector<int>& l, vector<int>& r) {
        vector<bool> vRet(l.size(), true);
        
        for(int i=0;i<l.size();i++)
        {
            vector<int> vTmp = vector<int>(nums.begin() + l[i], nums.begin() + r[i] + 1);
            std::sort(vTmp.begin(), vTmp.end());
            
            int diff = vTmp[0] - vTmp[1];
            for(int j=0;j<vTmp.size() - 1;j++)
            {
                if((vTmp[j] - vTmp[j+1]) != diff)
                {
                    vRet[i] = false;
                    break;
                }
            }
        }
        return vRet;
    }
};
