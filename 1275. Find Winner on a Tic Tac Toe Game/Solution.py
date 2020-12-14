class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]
        
        cur_player = 'X'
        
        for move in moves:
            board[move[0]][move[1]] = cur_player
            if cur_player == 'X':
                cur_player = 'O'
            else:
                cur_player = 'X'
        
        print(board)
        
        for row in board:
            if row == ['O', 'O', 'O']:
                return 'B'
            if row == ['X', 'X', 'X']:
                return 'A'
        
        for i in range(3):
            if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
                if board[0][i] == 'X':
                    return 'A'
                if board[0][i] == 'O':
                    return 'B'
        
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            if board[1][1] == 'X':
                return 'A'
            if board[1][1] == 'O':
                return 'B'
            
        if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            if board[1][1] == 'X':
                return 'A'
            if board[1][1] == 'O':
                return 'B'
        
        if len(moves) == 9:
            return 'Draw'
        else:
            return 'Pending'
        
