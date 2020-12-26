class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        N = len(words)
        
        for i in range(N):
            for j in range(i+1, N):
                if words[i] in words[j]:
                    if words[i] not in res:
                        res.append(words[i])
                    
                    
                if words[j] in words[i]:
                    if words[j] not in res:
                        res.append(words[j])
                    
        
        return res
            
        
