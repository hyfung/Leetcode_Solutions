class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        
        std::map<std::string, int> d;
        
        for (auto &v : paths)
        {
            d[v[0]] ++;
            d[v[1]] --;
            
        }
        
        for (auto &v : d)
        {
            if (v.second == -1)
            {
                return v.first;
            }
        }
     
    return "";
        
    }
};
