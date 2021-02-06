class Solution {
public:
    char slowestKey(vector<int>& releaseTimes, string keysPressed) {
        std::vector<int> duration(releaseTimes.size(), 0);
        
        duration[0] = releaseTimes[0];
        for (int i=1;i<releaseTimes.size();i++)
        {
            duration[i] = releaseTimes[i] - releaseTimes[i-1];
        }

        std::vector<char> longestKeys;
        int currentLongest = 0;
        for (int i=0;i<duration.size();i++)
        {
            if (duration[i] > currentLongest)
            {
                longestKeys.clear();
                longestKeys.push_back(keysPressed[i]);
                currentLongest = duration[i];
                continue;  
            }
            if (duration[i] == currentLongest)
            {
                longestKeys.push_back(keysPressed[i]);
            }
        }
        
        char maxKey = 0;
        for (auto &ch : longestKeys)
        {
            maxKey = maxKey < ch ? ch : maxKey;
        }
        
        return maxKey;
    }
};
