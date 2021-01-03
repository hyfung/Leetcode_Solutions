class Solution {
public:
    int balancedStringSplit(string s) {
        
        int l_cnt = 0;
        int r_cnt = 0;
        int ret = 0;
        
        for (auto &ch : s)
        {
            if (ch == 'L')
            {
                l_cnt++;
            }
            
            if (ch == 'R')
            {
                r_cnt++;
            }
            
            if (l_cnt == r_cnt)
            {
                l_cnt = 0;
                r_cnt = 0;
                ret ++;                    
            }
        
        return ret;
    }
};
