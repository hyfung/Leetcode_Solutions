class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        J_MAX = len(matrix)
        I_MAX = len(matrix[0])
        
        # Store the index of rows/columns to be set to 0
        i_ = set()
        j_ = set()
        
        # Look for 0s in the matrix and record it
        for j in range(J_MAX):
            for i in range(I_MAX):
                if matrix[j][i] == 0:
                    i_.add(i)
                    j_.add(j)
        
        # Update the matrix according to the stored row/col indexes
        for j in range(J_MAX):
            for i in range(I_MAX):
                if i in i_ or j in j_:
                    matrix[j][i] = 0
                    
            
