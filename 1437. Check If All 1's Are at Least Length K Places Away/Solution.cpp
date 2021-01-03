class Solution {
public:
    bool kLengthApart(vector<int>& nums, int k) {
        
        std::vector<int> pos;
        
        int cnt = 0;
        for(std::vector<int>::iterator it = nums.begin() ; it != nums.end(); ++it)
        {
            if(*it == 1)
            {
                pos.push_back(cnt);
            }
            cnt++;
        }
        
        if (pos.size() == 0)
            return true;
        
        for(int i=0;i < pos.size() - 1;i++)
        {
            if(pos[i+1] - pos[i] < (k + 1))
            {
                return false;
            }
        }
        
        return true;
        
    }
};
