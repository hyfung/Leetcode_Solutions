class Solution {
public:
    vector<int> sortArrayByParityII(vector<int>& A) {
        vector<int> vOdd;
        vector<int> vEven;
        vector<int> vSorted;
        
        vOdd.reserve(A.size()/2);
        vEven.reserve(A.size()/2);
        vSorted.reserve(A.size());
        
        for (auto &v : A)
        {
            if (v % 2 == 0)
            {
                vEven.push_back(v);
            }
            else
            {
                vOdd.push_back(v);
            }
        }
        
        for (int i=0;i<vOdd.size();i++)
        {
            vSorted.push_back(vEven[i]);
            vSorted.push_back(vOdd[i]);
        }
        
        return vSorted;
    }
};
