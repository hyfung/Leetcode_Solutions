class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def make_dict(string):
            pattern = dict()
            for char in string:
                pattern[char] = 1 if char not in pattern else pattern[char] + 1
            return pattern
        
        res = []
        
        p_dict = make_dict(p)
        
        for i in range(0, len(s)-len(p) + 1):
            s_tmp = s[i:i+len(p)]
            if make_dict(s_tmp) == p_dict:
                res.append(i)
        
        return res
