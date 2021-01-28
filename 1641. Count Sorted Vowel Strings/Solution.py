import itertools
class Solution:
    def countVowelStrings(self, n: int) -> int:
        return len(list(itertools.combinations_with_replacement("aeiou",n)))
    
