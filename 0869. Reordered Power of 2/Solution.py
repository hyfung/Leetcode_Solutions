class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        digits = [2**x for x in range(0,31)]
        
        def fingerprint(x):
            d = dict()
            
            for char in str(x):
                if char not in d:
                    d[char] = 1
                else:
                    d[char] += 1
            
            return d
        
        patterns = list()
        
        for digit in digits:
            patterns.append(fingerprint(digit))
        
        fp = fingerprint(N)
        
        for pattern in patterns:
            if fp == pattern:
                return True
        
        return False
