class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        increasing = True
        # Increasing?
        for i in range(0,len(A)-1):
            if A[i+1] < A[i]:
                increasing = False
        
        decreasing = True
        # Decreasing?
        for i in range(0, len(A)-1):
            if A[i+1] > A[i]:
                decreasing = False
        
        return increasing or decreasing
            
