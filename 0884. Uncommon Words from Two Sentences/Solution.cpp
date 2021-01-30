class Solution {
public:
    
    static vector<string> split(string sData, string sDelimiter)
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
    
    vector<string> uncommonFromSentences(string A, string B) {
        map<string, int> mWords;
        vector<string> vUncommon;
        
        vector<string> aToken = split(A, " ");
        vector<string> bToken = split(B, " ");
        
        for (auto &word : aToken)
        {
            mWords[word]++;
        }
        
        for (auto &word : bToken)
        {
            mWords[word]++;
        }
        
        for (auto &v : mWords)
        {
            if (v.second == 1)
            {
                vUncommon.push_back(v.first);
            }
        }
        
        return vUncommon;
    }
};
