class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        S, P = len(s), len(p)
        
        # S-P+1 round sliding window
        # Using hashmap
        
        def make_dict(string):
            pattern = dict()
            for i in 'abcdefghijklmnopqrsztuvwxyz':
                pattern[i] = 0
            for char in string:
                pattern[char] += 1
            return pattern
        
        res = []
        
        p_dict = make_dict(p)
        
        # Prime the dictionary
        s_dict = make_dict(s[:len(p)])
        
        assert len(p_dict) == len(s_dict)
        
        for i in range(0, len(s)-len(p)+1):
            if s_dict == p_dict:
                res.append(i)
            
            try:
                s_dict[s[i]] -= 1
                s_dict[s[i+P]] += 1
            except:
                pass
        
        return res
