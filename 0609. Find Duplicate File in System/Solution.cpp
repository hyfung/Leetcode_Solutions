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

std::string& rtrim(std::string& str, const std::string& chars = "\t\n\v\f\r ")
{
    str.erase(str.find_last_not_of(chars) + 1);
    return str;
}
 

class Solution {
public:
    vector<vector<string>> findDuplicate(vector<string>& paths) {
        std::map<std::string, std::vector<std::string>> hashmap;
        
        std::vector<vector<string>> ret;
        
        for (auto &path : paths)
        {
            auto tokens = split(path, " ");
            for (int i=1;i<tokens.size();i++)
            {
                auto current = split((tokens[0]+"/"+tokens[i]), "(");
                hashmap[rtrim(current[1], ")")].push_back(current[0]);
            }
        }
        
        for (auto & [k,v] : hashmap)
        {
            if (v.size() > 1)
            {
                ret.push_back(v);
            }
        }
        
        return ret;
        
    }
};
