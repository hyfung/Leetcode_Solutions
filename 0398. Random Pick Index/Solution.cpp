class Solution {
public:
    std::map<int, std::vector<int>> dict;
    
    Solution(vector<int>& nums)
    {
        
        for(int i=0;i<nums.size();i++)
        {
            auto search = dict.find(nums[i]);
            if(search != dict.end())
            {
                dict[nums[i]].push_back(i);
            }
            else
            {
                dict[nums[i]] = {i};
            }
        }
        
        
    }
    
    int pick(int target) {
        auto search = dict.find(target);
        
        return search->second[rand() % search->second.size()];
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * int param_1 = obj->pick(target);
 */
