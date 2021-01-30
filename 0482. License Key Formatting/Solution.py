class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        ret = ""
        
        S = S.upper().replace('-', '')
        print(S)
        print(S[-1*K:])
        
        while S:
            ret = "-" + S[-1*K:] + ret 
            S = S[:-1*K]
        
        return ret.lstrip('-')
        
