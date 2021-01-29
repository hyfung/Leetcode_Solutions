class Solution {
public:
    bool isOneBitCharacter(vector<int>& bits) {
        // Remove trailing zero
        // bits.pop_back();
        int i;
        
        for(i=0;i<bits.size()-1;i++)
        {
            i += bits[i];
        }
        
        return i == bits.size()-1;
        
    }
};
