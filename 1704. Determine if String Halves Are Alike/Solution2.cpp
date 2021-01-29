class Solution {
public:
    bool halvesAreAlike(string s) {
        std::set<char> sVowel{'a','e','i','o','u','A','E','I','O','U'};
        
        int iDemarc = s.size()/2;
        int iL = 0;
        int iR = 0;
        
        for(int i=0;i<s.size();i++)
        {
            auto res = sVowel.find(s[i]);
            if(res != sVowel.end())
            {
                if (i < iDemarc)
                    iL++;
                else
                    iR++;
            }
        }
        
        return iL == iR;    
        
    }
};
