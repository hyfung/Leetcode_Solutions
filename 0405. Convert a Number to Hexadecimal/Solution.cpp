class Solution {
public:
    string toHex(int num) {
        
        if (num == 0)
        {
            return std::string("0");
        }
        
        std::string ret = "";
        
        const unsigned char mapping[] = {
            '0', '1', '2', '3',
            '4', '5', '6', '7',
            '8', '9', 'a', 'b',
            'c', 'd', 'e', 'f'
        };
        
        for(int i = 3; i>=0;i--)
        {
            unsigned char lowCh = (num >> (i*8)) & 0x0F;
            unsigned char highCh = (num >> ((i*8)+4)) & 0x0F;
            
            ret += mapping[highCh];
            ret += mapping[lowCh];
        }
        
        return ret.erase(0, ret.find_first_not_of("0"));
        
    }
};
