class Solution {
public:
    int thirdMax(vector<int>& nums) {
        std::set<int> mymap;
        
        for (auto &v : nums)
        {
            mymap.insert(v);
        }
        
        std::vector<int> myvector;
        
        for (auto &v : mymap)
        {
            myvector.push_back(v);
        }
        
        std::sort(myvector.begin(), myvector.end());
        
        if (myvector.size() >= 3)
        {
            myvector.pop_back();
            myvector.pop_back();
            return myvector.back();
        }
        else
        {
            return myvector.back();
        }
        
        return 0;
    }
};
