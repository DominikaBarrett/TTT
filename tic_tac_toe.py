
#definiuje tablice jako liste list i wykluczam error
#zmieniam zakres odejmujac jeden na 0-8
#dzielac uzywajac modulo zwracam krotke definujac i/j jako kolumny i wiersze

def main():
    print("Witamy w fantastycznej grze.Made by Domi & Andrej!! Good luck")
    board = [["_" for _ in range(3)] for _ in range(3)]
    player_x = True
    game_over = False
    while not game_over:
        print_board(board)
#tak wyglada tablica pod"przykrywka"
#board = [
#   j          j     j
# i[0 | 0,  0  |  1,  0 | 2],
# i[1 |  0, 1  |  1,  1 | 2],
# i[2 | 0,  2 | 1,  2 | 2]
# ]
# przyklady
# 1 = > 0,0
# 4 = > 1,0
# 8 => 2,1
        try:
            move = convert_move(choose_move())
            get_move(move, player_x,board)
        except ValueError:
            print("\nTo miejsce jesr juz zajete, wybierz ponownie...\n")
            continue
        # print_board(board)
        game_over = is_win(board) or is_draw(board)
        player_x = not player_x


def convert_move(move):
    move -= 1
    return (move // 3, move % 3)
# print(convert_move(3))


def is_draw(board):
    for row in board:
        for val in row:
            if val == "_":
                return False
    print("\nREMIS!!!\n")
    print("\nGame OVER\n")
    return True


def is_win(board):
    winner = None
    for i in range(3):
        #horyzontalnie
        if board[i][0] ==board[i][1] ==board[i][2] and board[i][0] != "_":
            winner =board[i][0]
            break
    #vertikalnie
        if board[0][i] ==board[1][i] ==board[2][i] and board[0][i] != "_":
            winner =board[0][i]
            break
    #w poprzek
    if board[1][1] != "_":
        if (board[0][0] ==board[1][1] ==board[2][2] or board[0][2] ==board[1][1] ==board[2][0]):
            winner =board[1][1]
        if winner is not None:
            print_board(board)
            print(f"{winner} jetses zwyciesca!!!")
            return True
        return False


def get_move(move, player_x,board):
    #sprawdzam czy tablica jest pusta zanim ja wypelnoe x /y
    #move jest tuple
    i, j = move
    if board[i][j] == "_":
       board[i][j] = "X" if player_x else "O"
    else:
        raise ValueError


def print_board(board):
    for row in board:
        print(row)

#wybieram pole od 1 do 9 (input always returns a string!)

def choose_move():
    move = int(input("Wybierz pole: "))
    if not 1 <= move <= 9:
        raise ValueError
    return move

def play_again(restart):
    restart = input("Chcesz zagrac ponownie"(t/n)")
    if restart == "t" or restart == "Y":
        return True
    else:
        print("\n milego dnia\n")

if __name__ == "__main__":
    main()
