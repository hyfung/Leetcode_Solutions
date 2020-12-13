class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n == 1:
            return 0
        
        if n == 2:
            return 1
        
        matches = 0
        # If even
        if n % 2 == 0:
            matches += n/2
            matches += self.numberOfMatches(n/2)
        
        # If odd
        if n % 2 == 1:
            matches += n//2
            matches += self.numberOfMatches((n-1)/2 + 1)
        
        return int(matches)
        
