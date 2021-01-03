class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        d = dict()
        N = len(A)
        res = []
        
        for word in A:
            d_ = dict()
            
            for ch in word:
                if ch not in d_:
                    d_[ch] = 1
                else:
                    d_[ch] += 1
            
            for key in d_.keys():
                if key in d:
                    d[key] += [d_[key]]
                else:
                    d[key] = [d_[key]]
        
        # If a character has occured in all N words, get the least occurence
        for k,v in d.items():
            if len(v) == N:
                res += [k] * min(v)
        
        return res
