class Solution {
public:
    int numRookCaptures(vector<vector<char>>& board) {
        int iCapture = 0;
        vector<int> rook = {0,0};
        
        vector<vector<int>> directions = {{0,1}, {1,0}, {-1,0}, {0,-1}};
        
        for (int j=0;j<8;j++)
        {
            for (int i=0;i<8;i++)
            {
                if (board[j][i] == 'R')
                {
                    rook = {i,j};
                    cout << "Rook - X:" << rook[0] << " " << "Y:"<< rook[1] << endl;
                }
            }
        }
        
        for(auto &v: directions)
        {
            vector<int> rook_copy = vector<int>(rook);
            while(rook_copy[0] > 0 && rook_copy[0] < 7 && rook_copy[1] > 0 && rook_copy[1] < 7)
            {
                rook_copy[0] += v[0];
                rook_copy[1] += v[1];
                // break;
                if (board[rook_copy[1]][rook_copy[0]] == 'p')
                {
                    iCapture++;
                    break;
                }
                if (board[rook_copy[1]][rook_copy[0]] == 'B')
                {
                    break;
                }
            }
        }
        
        return iCapture;
    }
};
