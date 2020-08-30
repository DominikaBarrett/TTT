
#definiuje tablice jako liste list i wykluczam error
#zmieniam zakres odejmujac jeden na 0-8
#dzielac uzywajac modulo zwracam krotke definujac i/j jako kolumny i wiersze
def main():
    board = [["_" for _ in range(3)] for _ in range(3)]
    player_x = True
    while True:
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
            get_move(move, player_x, board)
        except ValueError:
            print("Prosze wybrac z przedzialu od 1-9")
        # print_board(board)
        player_x = not player_x


def convert_move(move):
    move -= 1
    return (move // 3, move % 3)
# print(convert_move(3))


def get_move(move, player_x, board):
    board[move[0]][move[1]] = "X" if player_x else "O"


def print_board(board):
    for row in board:
        print(row)

#wybieram pole od 1 do 9 (input always returns a string!)


def choose_move():
    move = int(input("Wybierz pole: "))
    if not 1 <= move <= 9:
        raise ValueError
    return move


if __name__ == "__main__":
    main()
