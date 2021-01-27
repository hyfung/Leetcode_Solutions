class Solution {
public:
    int findJudge(int N, vector<vector<int>>& trust) {
        std::set<int> sVoted;
        std::map<int, int> mVotes;
        
        for (auto &t : trust)
        {
            sVoted.insert(t[0]);
            mVotes[t[1]] += 1;
        }
        
        for (int i=1;i<N+1;i++)
        {
            auto search = sVoted.find(i);
            if (search == sVoted.end() && mVotes[i] == N-1)
            {
                return i;
            }
        }
        
        return -1;
    }
};
