class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = dict()
        
        for i,v in enumerate(numbers):
            if v not in d:
                d[v] = [i]
            else:
                d[v] += [i]
            
        for k in d.keys():
            if target-k in d.keys():
                if target-k != k:
                    return [min(d[k][0], d[target-k][0])+1, max(d[k][0], d[target-k][0])+1]
                else:
                    return [min(d[k])+1, max(d[k])+1]
            
        
