vector<string> split(string sData, string sDelimiter)
{
    char *pToken = NULL;

    uint uStringLength = strlen(sData.c_str());

    char aData[uStringLength + 1];
    vector<string> vTokens;
    vTokens.clear();

    memset(aData, 0x00, uStringLength + 1);
    memcpy(aData, sData.c_str(), uStringLength);

    pToken = strtok(aData, sDelimiter.c_str());
    while (pToken != NULL)
    {
        vTokens.push_back(pToken);
        pToken = strtok(NULL, sDelimiter.c_str());
    }

    if (pToken != NULL)
        delete pToken;

    return vTokens;
}

class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        vector<int> normalized;
        normalized.reserve(timePoints.size() * 2);
        
        for (const string timePoint : timePoints)
        {
            vector<string> hm = split(timePoint, ":");
            int hm_int = std::stoi(hm[0]) * 60 + std::stoi(hm[1]);
            normalized.push_back(hm_int);
            normalized.push_back(hm_int+1440);
        }
        
        std::sort(normalized.begin(), normalized.end());
        
        int min_diff = 214783647;
        
        for (int i=1;i<normalized.size();i++)
        {
            int diff = normalized[i] - normalized[i-1];
            if (diff < min_diff)
            {
                min_diff = diff;
            }
        }
        
        return min_diff;
    }
};
