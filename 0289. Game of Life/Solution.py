class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        HEIGHT = len(board)
        LENGTH = len(board[0])
        
        # print(HEIGHT, LENGTH)
        

        # Set up a padded board
        padded_board = []
        for i in range(0, HEIGHT+2):
            #Deepcopy
            padded_board.append([0] * (LENGTH+2))
        # print(padded_board)
        
        # Copy initial state to padded board
        for j in range(0, HEIGHT):
            for i in range(0, LENGTH):
                padded_board[j+1][i+1] = board[j][i]
        # print(padded_board)

        for j in range(1, HEIGHT+1):
            for i in range(1, LENGTH+1):
                neighbour = 0
                neighbour += padded_board[j][i+1]
                neighbour += padded_board[j][i-1]
                neighbour += padded_board[j+1][i]
                neighbour += padded_board[j-1][i]
                neighbour += padded_board[j+1][i+1]
                neighbour += padded_board[j-1][i-1]
                neighbour += padded_board[j+1][i-1]
                neighbour += padded_board[j-1][i+1]

                if padded_board[j][i] == 1:
                    if neighbour < 2:
                        board[j-1][i-1] = 0
                    if neighbour == 2 or neighbour == 3:
                        board[j-1][i-1] = 1
                    if neighbour > 3:
                        board[j-1][i-1] = 0
                if padded_board[j][i] == 0 and neighbour == 3:
                    board[j-1][i-1] = 1
                
