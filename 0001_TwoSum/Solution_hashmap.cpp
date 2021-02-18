class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
       std::map<int,int> hashmap;
        for (int i=0;i<nums.size();i++)
        {
            hashmap[nums[i]] = i;
        }
        
        for (int i=0;i<nums.size();i++)
        {
            int compliment = target - nums[i];
            
            auto it = hashmap.find(compliment);
            if (it != hashmap.end())
            {
                if (it->second != i)
                    return {i, it->second};
            }
        }
        
        return {0,0};
    }
};
