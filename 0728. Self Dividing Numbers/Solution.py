class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        
        for i in range(left, right+1):
            append = True
            
            if '0' in str(i):
                continue
                
            for ch in str(i):
                if i % int(ch) != 0:
                    append = False
            
            if append:
                res.append(i)
        
        return res
        
