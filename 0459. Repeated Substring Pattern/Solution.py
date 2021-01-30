class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s)):
            tmp = s.split(s[0:i])
            if "".join(tmp) is "":
                return True
        return False
        
