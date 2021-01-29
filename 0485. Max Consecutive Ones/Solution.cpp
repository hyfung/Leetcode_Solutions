class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int iCurLength = 0;
        int iRet = 0;
        
        for (auto &v : nums)
        {
            if (v == 1)
            {
                iCurLength += 1;
            }
            else
            {
                iRet = iRet < iCurLength ? iCurLength : iRet;
                iCurLength = 0;
            }
        }
        
        return iRet < iCurLength ? iCurLength : iRet;
    }
};
