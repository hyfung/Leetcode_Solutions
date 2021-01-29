class Solution {
public:
    bool isOneBitCharacter(vector<int>& bits) {
        bool expectNext = false;
        
        for(int i=0;i<bits.size();i++)
        {
            expectNext = false;
            if(bits[i] == 1)
            {
                expectNext = true;
                i++;
            }
        }
        
        return !expectNext;
    }
};
