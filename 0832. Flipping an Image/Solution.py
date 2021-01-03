class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            A[i] = A[i][::-1]
            
        for i in range(len(A)):
            A[i] = [0 if x == 1 else 1 for x in A[i]]
        
        return A
            
        
