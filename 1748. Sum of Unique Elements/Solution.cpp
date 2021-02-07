class Solution {
public:
    int sumOfUnique(vector<int>& nums) {
        std::map<int, int> elements;
        
        int sum = 0;
        
        for (auto &v : nums)
        {
            elements[v]++;
        }
        
        for (auto & [k,v] : elements)
        {
            if (v == 1)
            {
                sum += k;
            }
        }
        
        return sum;
    }
};
