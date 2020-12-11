import itertools

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return ""
        
        mapping = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        
        comb = []
        for digit in digits:
            comb.append(mapping[digit])
            
        return [''.join(x) for x in itertools.product(*comb)]
