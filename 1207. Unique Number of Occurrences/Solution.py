class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurence = dict()
        
        for number in arr:
            if number not in occurence:
                occurence[number] = 1
            else:
                occurence[number] += 1
        
        return len(occurence.values()) == len(set(occurence.values()))
    
