class Solution {
public:
    int busyStudent(vector<int>& startTime, vector<int>& endTime, int queryTime) {
        
        int i;
        int cnt = 0;
        
        for(i=0;i<startTime.size();i++)
        {
            if ((startTime.at(i) <= queryTime) && (endTime.at(i) >= queryTime))
            {
                cnt++;
            }
        }
        
        return cnt;
    }
};
