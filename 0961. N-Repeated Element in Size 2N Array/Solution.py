class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        N = len(A)//2
        
        occurence = dict()
        
        for i in A:
            # I forgot how to optimize this
            if i not in occurence:
                occurence[i] = 1
            else:
                occurence[i] += 1
            
            if occurence[i] == N:
                return i
