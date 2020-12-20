class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for i in range(numRows):
            # Allocating the necessary array
            res.append([0] * (i+1))
            res[i][0] = 1
            res[i][-1] = 1

        for i in range(numRows):
            if i <= 1:
                # Skip first 2 rows: 0 and 1
                continue

            for j in range(1, len(res[i]) -1):
                print(i, j)
                res[i][j] = res[i-1][j]+res[i-1][j-1]

        return res
