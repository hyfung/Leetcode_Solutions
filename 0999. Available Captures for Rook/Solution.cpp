class Solution {
public:
    int numRookCaptures(vector<vector<char>>& board) {
        int iCapture = 0;
        vector<int> vRookPosition = {0,0};
        
        // Four directions to look for pawn or bishop
        vector<vector<int>> directions = {{0,1}, {1,0}, {-1,0}, {0,-1}};
        
        //Scan for rook on the chessboard
        for (int j=0;j<8;j++)
        {
            for (int i=0;i<8;i++)
            {
                if (board[j][i] == 'R')
                {
                    // Rook located
                    vRookPosition = {i,j};
                    cout << "vRookPosition - X:" << vRookPosition[0] << " " << "Y:"<< vRookPosition[1] << endl;
                }
            }
        }
        
        for (auto &v: directions)
        {
            vector<int> vRookPosTmp = vector<int>(vRookPosition);
            while(vRookPosTmp[0] > 0 && vRookPosTmp[0] < 7 && vRookPosTmp[1] > 0 && vRookPosTmp[1] < 7)
            {
                vRookPosTmp[0] += v[0];
                vRookPosTmp[1] += v[1];
                // Check if we hit any pawn on the path, if so we increment counter and break
                if (board[vRookPosTmp[1]][vRookPosTmp[0]] == 'p')
                {
                    iCapture++;
                    break;
                }
                // Check if we hit any bishop on the path if so we break
                if (board[vRookPosTmp[1]][vRookPosTmp[0]] == 'B')
                {
                    break;
                }
            }
        }
        
        return iCapture;
    }
};
