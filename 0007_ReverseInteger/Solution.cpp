class Solution {
public:
    int reverse(int x) {
        if (x == -2147483648)
        {
            return 0;
        }
        try
        {
            int sign = 1;
            if (x < 0)
            {
                sign = -1;
                x *= -1;
            }
            string str = std::to_string(x);

            std::reverse(str.begin(), str.end());

            return std::stoi(str) * sign;    
        }
        catch (...)
        {
            return 0;
        }
        
    }
};
