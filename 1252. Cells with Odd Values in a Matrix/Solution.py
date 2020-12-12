class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        mat = []
        for i in range(0,n):
            mat.append(m * [0])
        
        def inc_row(x):
            for i in range(0, m):
                mat[x][i] += 1
        
        def inc_col(x):
            for i in range(0, n):
                mat[i][x] += 1
        
        # Incrementing rows
        for op in indices:
            inc_row(op[0])
            inc_col(op[1])
        
        # Finally calculating number of odd cells
        counter = 0
        for rows in mat:
            for ele in rows:
                if ele % 2 == 1:
                    counter += 1
        return counter
        
