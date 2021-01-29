class Solution {
public:
    string removeOuterParentheses(string S) {
        std::string sRes;
        sRes.reserve(S.size());
        int iCounter = 0;
        bool bOpen = false;
        
        for (const char &ch : S)
        {
            if (ch == '(')
            {
                if (!bOpen)
                {
                    bOpen = true;
                    continue;
                }
                else
                {
                    iCounter += 1;
                    sRes += '(';
                }
            }
            else
            {
                if (bOpen && iCounter == 0)
                {
                    bOpen = false;
                    continue;
                }
                else
                {
                    iCounter -= 1;
                    sRes += ')';
                }
            }
            
        }
        
        return sRes;
        
    }
};
