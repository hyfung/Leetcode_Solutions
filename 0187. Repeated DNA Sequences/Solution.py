class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        N = len(s)
        occur = dict()
        res = []
        
        for i in range(0, N-10+1):
            
            tmp = s[i:i+10]

            if tmp in occur:
                occur[tmp] += 1
            else:
                occur[tmp] = 1
                
        return [k for k,v in occur.items() if v > 1]
        
