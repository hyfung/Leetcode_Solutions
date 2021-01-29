#define OFF 0
#define ON 1
#define BLUE 2

class Solution {
public:
    bool onlyBlue(vector<int>& light)
    {
        for (auto &v : light)
        {
            if (v == 1)
                return false;
        }
        return true;
    }
    
    
    int numTimesAllBlue(vector<int>& light) {
        vector<int> vStates(light.size(), 0);
        int iMoment = 0;
        
        for (auto &v : light)
        {
            // 1: Toggle the light
            vStates[v-1] = ON;
            
            // 2: Check if all previous bulbs are on too
            int iOnUntil = -1;
            
            for (int i=0;i<vStates.size();i++)
            {
                if (vStates[i])
                {
                    iOnUntil += 1;
                }
                else
                {
                    break;
                }
            }
            
            if (iOnUntil >= 0)
            {
                for(int i=0;i<iOnUntil+1;i++)
                {
                    vStates[i] = BLUE;
                }
            }
            if (onlyBlue(vStates))
                iMoment++;
        }
        
        return iMoment; 
        
    }
};
