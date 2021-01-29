class KthLargest {
public:
    std::vector<int> vNums;
    int k;
    
    KthLargest(int k, vector<int>& nums) {
        vNums = vector<int>(nums);
        std::sort(vNums.begin(),vNums.end());
        this->k = k;
    }
    
    int add(int val) {
        vNums.push_back(val);
        std::sort(vNums.begin(),vNums.end());
        return vNums[vNums.size()-k];
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */
