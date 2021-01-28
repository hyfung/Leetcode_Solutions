#include <cmath>
#include <cstdlib>

class Solution {
public:
    string reformat(string s) {
        string sDigit;
        string sChar;
        string sRet;
        
        for(int i=0;i<s.size();i++)
        {
            //Less than 58 is digit
            if (s[i] < 58)
            {
                sDigit += s[i];
            }
            else
            {
                sChar += s[i];    
            }
        }
        
        if (abs(int(sDigit.size()-sChar.size())) > 1)
            return "";
            
        
        if (sDigit.size() == sChar.size())
        {
                for(int i=0;i<sChar.size();i++)
                {
                    sRet += sChar[i];
                    sRet += sDigit[i];
                }
        }                
        else if (sDigit.size() > sChar.size())
        {
            sRet += sDigit[sDigit.size()-1];
            for(int i=0;i<sChar.size();i++)
            {
                sRet += sChar[i];
                sRet += sDigit[i];
            }
        }
            
        else
        {
            sRet += sChar[sChar.size()-1];
            for(int i=0;i<sDigit.size();i++)
            {
                sRet += sDigit[i];
                sRet += sChar[i];
            }
        }      
        
        return sRet;
        
    }
};
