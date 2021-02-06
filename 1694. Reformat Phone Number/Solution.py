class Solution:
    def reformatNumber(self, number: str) -> str:
        x = number.replace(" ", "").replace("-", "")
        ret = ""
        
        print(x)
        
        while len(x) > 4:
            ret += x[0:3] + "-"
            x = x[3:]
        if len(x) == 2:
            ret += x
        if len(x) == 3:
            ret += x
        if len(x) == 4:
            ret += x[0:2] + "-" + x[2:]
            
        return ret
        
        
        
