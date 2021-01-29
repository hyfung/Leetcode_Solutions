class Solution {
public:
    int longestPalindrome(string s) {
        std::map<char, int> mCh;
        bool bHasOdd = false;
        int iRet = 0;
            
        for (auto &ch : s)
        {
            mCh[ch] += 1;
        }
        
        for (auto &[k,v]: mCh)
        {
            if (v%2 == 1 && !bHasOdd)
            {
                bHasOdd = true;
                iRet += 1;
            }
            
            iRet += int(v / 2) * 2;            
        }
        
        return iRet;
    }
};
