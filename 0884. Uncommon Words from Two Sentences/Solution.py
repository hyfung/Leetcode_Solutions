class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        d = dict()
        
        for word in A.split(' '):
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1
                
        for word in B.split(' '):
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1
                 
        return [k for k,v in d.items() if v == 1]
        
