
#definiuje tablice jako liste list i wykluczam error
#zmieniam zakres odejmujac jeden na 0-8
#dzielac uzywajac modulo zwracam krotke definujac i/j jako kolumny i wiersze
def main():
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
            if move != (-1, -1):
                get_move(move, player_x, board)
            else:
                print("Podaj wartość z zakresu od 1 do 9!")
        except ValueError:
            print("To miejsce jest juz zajete, wybierz ponownie...")
            continue
        game_over = is_win(board) or is_draw(board)
        player_x = not player_x


def convert_move(move):
    if move > -1:
        move -= 1
        return move // 3, move % 3
    else:
        return -1, -1


def is_draw(board):
    for row in board:
        for val in row:
            if val == "_":
                return False
    print("REMIS!!!")
    return True


def is_win(board):
    winner = None
    for i in range(3):
        #horyzontalnie
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "_":
            winner = board[i][0]
            break
    #vertikalnie
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "_":
            winner = board[0][i]
            break
    #w poprzek
    if board[1][1] != "_":
        if (board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]):
            winner = board[1][1]
        if winner is not None:
            print_board(board)
            print(f"{winner} jetses zwyciesca!!!")
            return True
        return False


def get_move(move, player_x, board):
    #sprawdzam czy tablica jest pusta zanim ja wypelnoe x /y
    #move jest tuple
    i, j = move
    if board[i][j] == "_":
        board[i][j] = "X" if player_x else "O"
    else:
        raise ValueError


def print_board(board):
    cell_0 = 0
    cell_1 = 1
    cell_2 = 2
    line = "---+---+---"
    counter = 0
    numbers = 1
    for row in board:
        if counter == 0:
            template = f'    \033[36m{counter + 1}\033[0m | {counter + 2} | {counter + 3}'
        elif counter == 1:
            template = f'    {counter + 3} | {counter + 4} | {counter + 5}'
        else:
            template = f'    {counter + 5} | {counter + 6} | {counter + 7}'
        print(f' {row[cell_0]} | {row[cell_1]} | {row[cell_2]} {template}')
        if counter < 2:
            print(f'{line}   {line}')
        counter += 1
        numbers += 1


#wybieram pole od 1 do 9 (input always returns a string!)


def choose_move():
    try:
        move = int(input("Wybierz pole: "))
        if 1 <= move <= 9:
            return move
        else:
            return -1
    except ValueError:
        return -1


if __name__ == "__main__":
    main()
