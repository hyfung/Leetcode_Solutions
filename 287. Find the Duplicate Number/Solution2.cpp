/*
Set based solution
*/

class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        std::set<int> occured;
        
        std::set<int>::iterator it;
        for (auto &v: nums)
        {
            if (occured.find(v) == occured.end())
            {
                occured.insert(v);
            }
            
            else return v;
        }
        return -1;
    }
};
