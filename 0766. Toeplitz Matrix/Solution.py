class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # Matrix in the form of [j][i]
        
        I_MAX = len(matrix[0])
        J_MAX = len(matrix)
        
        for j in range(J_MAX):
            for i in range(I_MAX):
                try:
                    if matrix[j][i] != matrix[j+1][i+1]:
                        return False
                except:
                    pass
        
        for i in range(I_MAX):
            for j in range(J_MAX):
                try:
                    if matrix[j][i] != matrix[j+1][i+1]:
                        return False
                except:
                    pass
        
        return True
        
