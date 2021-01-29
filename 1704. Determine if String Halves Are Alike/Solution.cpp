class Solution {
public:
    bool halvesAreAlike(string s) {
        std::set<char> sVowel{'a','e','i','o','u','A','E','I','O','U'};
        
        string sLeft;
        string sRight;
        sLeft.reserve(s.size()/2);
        sRight.reserve(s.size()/2);
        
        sLeft = s.substr(0,s.size()/2);
        sRight = s.substr(s.size()/2, s.size());
        
        int iL = 0;
        int iR = 0;
        
        // cout << sLeft << endl;
        // cout << sRight << endl;
        
        for(int i=0;i<s.size()/2;i++)
        {
            auto res = sVowel.find(sLeft[i]);
            if(res != sVowel.end())
            {
                iL += 1;
            }
            
            res = sVowel.find(sRight[i]);
            if(res != sVowel.end())
            {
                iR += 1;
            }
        }
        
        return iL == iR;
        
    }
};
