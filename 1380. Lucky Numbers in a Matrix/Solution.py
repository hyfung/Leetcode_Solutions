class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        ls = []
        for j in range(m):
            for i in range(n):
                if matrix[j][i] == min(matrix[j]) and matrix[j][i] == max([x[i] for x in matrix]):
                    ls.append(matrix[j][i])
        return ls
