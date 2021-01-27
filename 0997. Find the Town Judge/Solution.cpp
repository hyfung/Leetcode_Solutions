class Solution {
public:
    int findJudge(int N, vector<vector<int>>& trust) {
        std::set<int> sVoted;
        std::map<int, int> mVotes;
        
        
        // First we build a data frame
        for (auto &t : trust)
        {
            sVoted.insert(t[0]);
            mVotes[t[1]] += 1;
        }
        
        // Then check for two criteria
        // 1. Judge has not voted
        // 2. Judge has N-1 votes
        for (int i=1;i<N+1;i++)
        {
            auto search = sVoted.find(i);
            if (search == sVoted.end() && mVotes[i] == N-1)
            {
                return i;
            }
        }
        
        // Otherwise we return not found
        return -1;
    }
};
