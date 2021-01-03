#include <map>

class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        
        std::map<int, int> hashmap;
        std::vector<int> res;
        
        for (std::vector<int>::iterator it = nums.begin() ; it != nums.end(); ++it)
        {
            auto search = hashmap.find(*it);
                if (search != hashmap.end())
                {
                    hashmap[*it]++;
                } else
                {
                    hashmap[*it] = 1;                    
                }
        }
        
        for (std::map<int, int>::iterator it = hashmap.begin() ; it != hashmap.end(); ++it)
        {
            if (it->second == 1)
            {
                res.push_back(it->first);
            }
        }
        
        return res;
    }
};
