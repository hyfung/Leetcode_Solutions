class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        vector<int> flatten;
        flatten.reserve(matrix.size() * matrix[0].size());
        
        for (auto &row : matrix)
        {
            if (std::binary_search(row.begin(), row.end(), target))
                return true;
        
        }
        return false;
    }
};
