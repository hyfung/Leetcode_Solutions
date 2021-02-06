class Solution {
public:
    vector<vector<int>> queensAttacktheKing(vector<vector<int>>& queens, vector<int>& king) {
        // We look in 8 directions
        vector<vector<int>> directions = {{-1,-1},{-1,0},{-1,1},{0,1},{1,1},{1,0},{1,-1},{0,-1}};
        
        // Container to store attackable queens
        vector<vector<int>> ret;
        
        // Step 1: Convert the queens vector into a set for O(1) search
        std::set<vector<int>> queen_set;
        for (auto &v : queens)
        {
            queen_set.insert(v);
        }
        
        // For each direction we do a search        
        for (const vector<int> direction : directions)
        {
            // Store the starting point
            vector<int> tmp_king(king);
            
            // While our king is still within the chessboard
            while(tmp_king[0] >= 0 && tmp_king[1] >= 0 && tmp_king[0] <= 7 && tmp_king[1] <= 7)
            {
                // Check if this grid has a queen
                if (queen_set.find(tmp_king) != queen_set.end())
                {
                    // If so we add that to the list and break out from this direction
                    ret.push_back(tmp_king);
                    break;
                }
                // Move a step    
                tmp_king[0] += direction[0];
                tmp_king[1] += direction[1];
            }
        }
        
        return ret;
    }
};
