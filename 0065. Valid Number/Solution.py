class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip(' ')
        try:
            float(s)
            return True
        except:
            return False
        
