#include <cmath>

class Solution {
public:
    vector<int> constructRectangle(int area) {
        int iMaxWidth = (int)std::sqrt(area);
        
        int iL, iW;
        
        for(int i=iMaxWidth+1;i>-1;i--)
        {
            if((area % i) == 0)
            {
                if (i < area/i)
                    return vector<int>{area/i, i};
                else
                    return vector<int>{i, area/i};
            }
        }
        
        return vector<int>{0,0};
    }
};
