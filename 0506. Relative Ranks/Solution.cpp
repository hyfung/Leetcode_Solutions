class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& nums) {
        vector<int>scores = vector<int>(nums);
        std::sort(scores.begin(), scores.end(), [](int a,int b){return a > b;});
        std::map<int, std::string> mapping;
        std::vector<string> res;
        res.reserve(nums.size());
        
        for (int i=0;i<scores.size();i++)
        {
            int v = scores[i];
            if (i==0)
            {
                mapping[v] = "Gold Medal";
            }
            else if (i==1)
            {
                mapping[v] = "Silver Medal";
            }
            else if (i==2)
            {
                mapping[v] = "Bronze Medal";
            }
            else
            {
                mapping[v] = std::to_string(i+1);
            }
        }
        
        for (int i=0;i<nums.size();i++)
        {
            res.push_back(mapping[nums[i]]);
        }
        
        return res;
    }
};
