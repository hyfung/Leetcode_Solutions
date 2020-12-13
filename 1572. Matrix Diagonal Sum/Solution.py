class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        # If N is odd
        if len(mat) % 2 == 1:
            for i in range(len(mat)):
                sum += mat[i][i]
                sum += mat[i][len(mat)-1-i]
            sum -= mat[len(mat)//2][len(mat)//2]
        
        # If N is even
        else:
            for i in range(len(mat)):
                sum += mat[i][i]
                sum += mat[i][len(mat)-1-i]
        
        return sum
