using namespace std;

class Solution {
public:    
    vector<string> split (string s, string delimiter) {
    size_t pos_start = 0, pos_end, delim_len = delimiter.length();
    string token;
    vector<string> res;

    while ((pos_end = s.find (delimiter, pos_start)) != string::npos) {
        token = s.substr (pos_start, pos_end - pos_start);
        pos_start = pos_end + delim_len;
        res.push_back (token);
    }

    res.push_back (s.substr (pos_start));
    return res;
    }
    
    int compareVersion(string version1, string version2) {
        vector<string> v1 = split(version1, ".");
        vector<string> v2 = split(version2, ".");
        
        vector<int> iv1;
        vector<int> iv2;
        
        for (const auto i: v1)
        {
            iv1.push_back(std::stoi(i));
        }
        
        for (const auto i: v2)
        {
            iv2.push_back(std::stoi(i));
        }
        
        int len_v1 = iv1.size();
        int len_v2 = iv2.size();
        
        if (len_v1 > len_v2)
        {
            for(int i=0;i<abs(len_v1-len_v2);i++)
                iv2.push_back(0);
        }
        
        if (len_v2 > len_v1)
        {
            for(int i=0;i<abs(len_v1-len_v2);i++)
                iv1.push_back(0);
        }
        
        for(int i=0;i<iv1.size();i++)
        {
            if (iv1[i] > iv2[i])
                return 1;
            if (iv1[i] < iv2[i])
                return -1;
        }
        
        return 0;
    }
};
