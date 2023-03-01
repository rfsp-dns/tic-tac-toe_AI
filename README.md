# TIC TAC TOE WITH ADVANCED AI - PYTHON

The AI is programmed by "IF" statements like this:

if board[1][1] == "X":
        if board[2][0] == "X":
            row, col = 0, 2
            if board[row][col] == "_":
                board[row][col] = "O"
                return
            else:
                if board[0][1] == "X":
                    row, col = 2, 1
                    if board[row][col] == "_":
                        board[row][col] = "O"
                        return
                    else:
                        if board[1][0] == "X":
                            row, col = 1, 2
                            if board[row][col] == "_":
                                board[row][col] = "O"
                                return
                        elif board[1][2] == "X":
                            row, col = 1, 0
                            if board[row][col] == "_":
                                board[row][col] = "O"
                                return
                        else:
                            while True :
                                row, col = random.randint(0,2), random.randint(0,2)
                                if board[row][col] == "_":
                                    board[row][col] = "O"
                                    return
                                    
The AI has a lot of "IF" and some tatics to make the player draw, for this version the AI detets the center tatic and block its as many possible ways.
But doing "IF" is not a solution because it can be suprass by not doing what in the "IF" says, because if the AI doesn't detect some strategies that i put in she automatically will do a random posision :

while True :
        row, col = random.randint(0,2), random.randint(0,2)
        if board[row][col] == "_":
            board[row][col] = "O"
            return
