class Solution:
    def myAtoi(self, s: str) -> int:
        # First strip off all leading whitespaces
        s = s.lstrip(' ')
        if s == "":
            return 0
        
        sign = ''
        if s[0] == '+' or s[0] == '-':
            sign = s[0]
            s = s[1:]
        
        # Convert to lowercase for easier differentiation
        s = s.lower()
        
        # Remove anything after first whitespace
        for i in 'abcdefghijklmnopqrstuvwxyz+- ':
            s = s.split(i)[0]
        
        s = s.rstrip('-')
        s = sign + s
        
        print(s)
        
        try:
            if float(s) < 0:
                return max(-2147483648, int(float(s)))
            elif float(s) > 2147483647:
                return 2147483647
            return int(float(s))
        except:
            return 0
        
