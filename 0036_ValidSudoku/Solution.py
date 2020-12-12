
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def valid_list(mylist):
            checker = {
            '1': 0, '2': 0, '3': 0,
            '4': 0, '5': 0, '6': 0,
            '7': 0, '8': 0, '9': 0,
            '.': 0
            }

            for item in mylist:
                checker[item] += 1

            checker['.'] = 0

            for k,v in checker.items():
                if v > 1:
                    return False
            return True


        def get_col(col_id):
            return [row[col_id] for row in board]

        def get_row(row_id):
            return board[row_id]

        def get_grid(x,y):
            x *= 3
            y *= 3
            return [
                board[y][x], board[y][x+1], board[y][x+2],
                board[y+1][x], board[y+1][x+1], board[y+1][x+2],
                board[y+2][x], board[y+2][x+1], board[y+2][x+2],
            ]

        # Check rows
        for i in range(0,9):
            if not valid_list(get_row(i)):
                return False

        # Check columns
        for i in range(0,9):
            if not valid_list(get_col(i)):
                return False

        # Check grid
        for i in range(0,3):
            for j in range(0,3):
                if not valid_list(get_grid(i,j)):
                    return False

        return True
