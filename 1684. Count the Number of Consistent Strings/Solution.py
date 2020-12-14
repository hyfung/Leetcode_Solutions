class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        counter = 0
        for word in words:
            if len([x for x in word if x not in allowed]) > 0:
                continue
            else:
                counter += 1
                
        return counter
        
