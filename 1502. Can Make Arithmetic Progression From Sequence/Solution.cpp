class Solution {
public:
    bool canMakeArithmeticProgression(vector<int>& arr) {
        // First we sort the array
        std::sort(arr.begin(), arr.end());
        
        // Then check if it is arithmetic progressive
        
        for (int i = 0;i < arr.size() - 2; i++)
        {
            if ((arr[i+2] - arr[i+1]) != (arr[i+1] - arr[i]))
                return false;
        }
        return true;
    }
};
