class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split(' ')):
            return False
        
        pat = dict()
        s = s.split(' ')
        for i,v in enumerate(pattern):
            if v not in pat:
                pat[v] = s[i]
            else:
                if pat[v] != s[i]:
                    return False
        if len(pat.keys()) != len(set(pat.values())):
            return False
        return True
                
        
