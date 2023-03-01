import random, os, time

#CONTRUÇÃO DA MESA DE JOGO
def create_board():
    return [["_" for _ in range(3)] for _ in range(3)]


#FUNÇÃO PARA A APRESENTAÇÃO DA MESA DE JOGO
def draw_board():
    for row in board:
        print(" ".join(row))

#MODO MANUAL 1V1
def get_move(jogador):
    while True:
        move = input("\n"+f"{jogador}, insere o teu movimento (linha coluna): ")
        if str(move) == ".sair" : 
            return ".sair"
        else:
            try:
                row, col = map(int, move.split())
                row -= 1 
                col -= 1
                if row in [0, 1, 2] and col in [0, 1, 2]:
                    if board[row][col] == "_":
                        board[row][col] = jogador
                        return
                    else:
                        print("O espaço está ocupado. Tenta denovo!")
                else:
                    print("Movimento inválido. Tenta denovo!")
            except ValueError:
                print("Inserção inválida. Tenta denovo!")

#MODO INTELIGENCIA ARTIFICIAL FACIL
def get_ai_move():
    while True:
        row, col = random.randint(0, 2), random.randint(0, 2)
        if board[row][col] == "_":
            board[row][col] = "O"
            return
        

def get_ai_moving_advanced():
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
        elif board[2][2] == "X":
            row, col = 0, 0
            if board[row][col] == "_":
                board[row][col] = "O"
                return
            else:
                while True :
                    row, col = random.randint(0,2), random.randint(0,2)
                    if board[row][col] == "_":
                        board[row][col] = "O"
                        return
        elif board[0][1] == "X":
            row, col = 2, 1
            if board[row][col] == "_":
                board[row][col] = "O"
                return
            else:
                while True :
                    row, col = random.randint(0,2), random.randint(0,2)
                    if board[row][col] == "_":
                        board[row][col] = "O"
                        return
        elif board[0][0] == "X":
            row, col = 2, 2
            if board[row][col] == "_":
                board[row][col] = "O"
                return
            else:
                while True :
                    row, col = random.randint(0,2), random.randint(0,2)
                    if board[row][col] == "_":
                        board[row][col] = "O"
                        return
        elif board[0][2] == "X":
            row, col = 2, 0
            if board[row][col] == "_":
                board[row][col] = "O"
                return
            else:
                while True :
                    row, col = random.randint(0,2), random.randint(0,2)
                    if board[row][col] == "_":
                        board[row][col] = "O"
                        return
        elif board[2][1] == "X" :
            row, col = 0, 1
            if board[row][col] == "_":
                board[row][col] = "O"
                return
            else:
                while True :
                    row, col = random.randint(0,2), random.randint(0,2)
                    if board[row][col] == "_":
                        board[row][col] = "O"
                        return
        elif board[1][0] == "X":
            row, col = 1, 2
            if board[row][col] == "_":
                board[row][col] = "O"
                return
            else:
                while True :
                    row, col = random.randint(0,2), random.randint(0,2)
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
        else:
            while True :
                row, col = random.randint(0,2), random.randint(0,2)
                if row != 1 and col != 1:
                    if board[row][col] == "_":
                        board[row][col] = "O"
                        return
    elif board[0][0] == "X":
        if board[2][2] == "X":
            row, col = 1, 1
            if board[row][col] == "_":
                board[row][col] = "O"
                return
            else:
                while True :
                    row, col = random.randint(0,2), random.randint(0,2)
                    if board[row][col] == "_":
                        board[row][col] = "O"
                        return
        elif board[0][2] == "X":
            row, col = 0, 1
            if board[row][col] == "_":
                board[row][col] = "O"
                return
            else:
                while True :
                    row, col = random.randint(0,2), random.randint(0,2)
                    if board[row][col] == "_":
                        board[row][col] = "O"
                        return
        elif board[2][0] == "X":
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
        else:
            while True :
                row, col = random.randint(0,2), random.randint(0,2)
                if board[row][col] == "_":
                    board[row][col] = "O"
                    return
    elif board[0][2] == "X":
        if board[0][0] == "X":
            row, col = 0, 1
            if board[row][col] == "_":
                board[row][col] = "O"
                return
            else:
                while True :
                    row, col = random.randint(0,2), random.randint(0,2)
                    if board[row][col] == "_":
                        board[row][col] = "O"
                        return
        elif board[2][0] == "X":
            row, col = 1, 1
            if board[row][col] == "_":
                board[row][col] = "O"
                return
            else:
                while True :
                    row, col = random.randint(0,2), random.randint(0,2)
                    if board[row][col] == "_":
                        board[row][col] = "O"
                        return
        elif board[2][2] == "X":
            row, col = 1, 2
            if board[row][col] == "_":
                board[row][col] = "O"
                return
            else:
                while True :
                    row, col = random.randint(0,2), random.randint(0,2)
                    if board[row][col] == "_":
                        board[row][col] = "O"
                        return
        else:
            while True :
                row, col = random.randint(0,2), random.randint(0,2)
                if board[row][col] == "_":
                    board[row][col] = "O"
                    return  
    elif board[2][2] == "X":
        if board[0][0] == "X":
            row, col = 1, 1
            if board[row][col] == "_":
                board[row][col] = "O"
                return
            else:
                while True :
                    row, col = random.randint(0,2), random.randint(0,2)
                    if board[row][col] == "_":
                        board[row][col] = "O"
                        return
        elif board[0][2] == "X":
            row, col = 1, 2
            if board[row][col] == "_":
                board[row][col] = "O"
                return
            else:
                while True :
                    row, col = random.randint(0,2), random.randint(0,2)
                    if board[row][col] == "_":
                        board[row][col] = "O"
                        return
        elif board[2][0] == "X":
            row, col = 2, 1
            if board[row][col] == "_":
                board[row][col] = "O"
                return
            else:
                while True :
                    row, col = random.randint(0,2), random.randint(0,2)
                    if board[row][col] == "_":
                        board[row][col] = "O"
                        return
        else:
            while True :
                row, col = random.randint(0,2), random.randint(0,2)
                if board[row][col] == "_":
                    board[row][col] = "O"
                    return
    elif board[2][0] == "X":
        if board[0][0] == "X":
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
        elif board[0][2] == "X":
            row, col = 1, 1
            if board[row][col] == "_":
                board[row][col] = "O"
                return
            else:
                while True :
                    row, col = random.randint(0,2), random.randint(0,2)
                    if board[row][col] == "_":
                        board[row][col] = "O"
                        return
        elif board[2][2] == "X":
            row, col = 2, 1
            if board[row][col] == "_":
                board[row][col] = "O"
                return
            else:
                while True :
                    row, col = random.randint(0,2), random.randint(0,2)
                    if board[row][col] == "_":
                        board[row][col] = "O"
                        return
        else:
            while True :
                row, col = random.randint(0,2), random.randint(0,2)
                if board[row][col] == "_":
                    board[row][col] = "O"
                    return   
    else:
        while True :
            row, col = random.randint(0,2), random.randint(0,2)
            if row and col != 1:
                if board[row][col] == "_":
                    board[row][col] = "O"
                    return

#MOVIMENTO DO JOGADOR
def get_jogador_move():
    while True:
        move = input("\n1Jogador, insere o teu movimento (linha coluna): ")
        if str(move) == ".sair" : 
            return ".sair"
        else:
            try:
                row, col = map(int, move.split())
                row -= 1 
                col -= 1
                if row in [0, 1, 2] and col in [0, 1, 2]:
                    if board[row][col] == "_":
                        board[row][col] = "X"
                        return
                    else:
                        print("O espaço está ocupado. Tenta denovo!")
                else:
                    print("Movimento inválido. Tenta denovo!")
            except ValueError:
                print("Inserção inválida. Tenta denovo!")

#VERIFICAÇÃO DE QUEM GANHOU
def has_won(jogador):
    # verificar as linhas
    for row in board:
        if row == [jogador, jogador, jogador]:
            return True
    # verificar as colunas
    for col in range(3):
        if board[0][col] == jogador and board[1][col] == jogador and board[2][col] == jogador:
            return True
    # verificar as diagonais
    if board[0][0] == jogador and board[1][1] == jogador and board[2][2] == jogador:
        return True
    if board[0][2] == jogador and board[1][1] == jogador and board[2][0] == jogador:
        return True
    return False

#VERIFICAÇÃO DE EMPATE
def is_full():
    for row in board:
        if "_" in row:
            return False
    return True

#FUNÇÃO PRINCIPAL
def main():
    global board
    while True:
        os.system("cls")
        board = create_board()
        print('''
Jogo da velha
----------------
1. Jogar contra Jogador
2. Jogar contra AI
3. Jogar contra AI Avançada
4. Sair

''')
        op = int(input("Opção : "))
        if op == 1:
            os.system("cls")
            draw_board()
            while True:
                if is_full():
                    print("Parece que o jogo ficou empatado.")
                    time.sleep(2)
                    os.system("cls")
                    break
                p1 = get_move("X")
                if p1 == ".sair":
                    break
                if has_won("X"):
                    print("O X ganhou!")
                    time.sleep(2)
                    os.system("cls")
                    break
                if is_full():
                    print("Parece que o jogo ficou empatado.")
                    time.sleep(2)
                    break
                time.sleep(0.3)
                os.system("cls")
                draw_board()
                p2 = get_move("O")
                if p2 == ".sair":
                    break
                if has_won("O"):
                    print("O O ganhou!")
                    time.sleep(2)
                    os.system("cls")
                    break
                if is_full():
                    print("Parece que o jogo ficou empatado.")
                    time.sleep(2)
                    os.system("cls")
                    break
                time.sleep(0.3)
                os.system("cls")
                draw_board()
        elif op == 2:
            os.system("cls")
            draw_board()
            while True:
                if is_full():
                    print("Parece que o jogo ficou empatado.")
                    time.sleep(2)
                    break
                f = get_jogador_move()
                if f == ".sair":
                    break
                if has_won("X"):
                    os.system("cls")
                    draw_board()
                    print("Tu ganhaste!")
                    time.sleep(2)
                    os.system("cls")
                    break
                if is_full():
                    print("Parece que o jogo ficou empatado.")
                    time.sleep(2)
                    break
                get_ai_move()
                if has_won("O"):
                    print("A AI ganhou. Tenta para a próxima!")
                    time.sleep(2)
                    os.system("cls")
                    break
                if is_full():
                    print("Parece que o jogo ficou empatado.")
                    time.sleep(2)
                    break
                time.sleep(0.3)
                os.system("cls")
                draw_board()
        elif op == 3:
            os.system("cls")
            draw_board()
            while True:
                if is_full():
                    print("Parece que o jogo ficou empatado.")
                    time.sleep(2)
                    break
                f = get_jogador_move()
                if f == ".sair":
                    break
                if has_won("X"):
                    os.system("cls")
                    draw_board()
                    print("Tu ganhaste!")
                    time.sleep(2)
                    os.system("cls")
                    break
                if is_full():
                    print("Parece que o jogo ficou empatado.")
                    time.sleep(2)
                    break
                get_ai_moving_advanced()
                if has_won("O"):
                    print("A AI ganhou. Tenta para a próxima!")
                    time.sleep(2)
                    os.system("cls")
                    break
                if is_full():
                    print("Parece que o jogo ficou empatado.")
                    time.sleep(2)
                    break
                time.sleep(0.3)
                os.system("cls")
                draw_board()

        elif op == 4:
            break

main()