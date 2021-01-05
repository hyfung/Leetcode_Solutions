class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        d = dict()
        
        for path in paths:
            if path[0] not in d:
                d[path[0]] = 1
            else:
                d[path[0]] += 1
            
            if path[1] not in d:
                d[path[1]] = -1
            else:
                d[path[1]] -= 1
                
        for k,v in d.items():
            if v == -1:
                return k
        
