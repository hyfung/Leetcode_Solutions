#include <iostream>
#include <vector>

class Solution {
public:
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

    string simplifyPath(string path) {
        vector<string> paths;
        string sRet = "";
        
        auto tokens = split(path, "/");
        
        for (auto &v : tokens)
        {
            if (v == ".")
            {
                continue;
            }
            else if (v == "..")
            {
                if (paths.size() == 0)
                    continue;
                else
                    paths.pop_back();
            }
            else
            {
                paths.push_back(v);
            }
        }
        
        for (auto &v : paths)
        {
            sRet += "/" + v;
        }
        
        if (sRet == "")
            sRet += "/";
        
        return sRet;
    }
};
