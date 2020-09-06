
#definiuje tablice jako liste list i wykluczam error
#zmieniam zakres odejmujac jeden na 0-8
#dzielac uzywajac modulo zwracam krotke definujac i/j jako kolumny i wiersze
import sys
import os


def clear_terminal():
    os.system("cls || clear")


def main():
    user_name()
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print_instructions()
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    board = [["_" for _ in range(3)] for _ in range(3)]
    player_x = True
    game_over = False

    while not game_over:

        clear_terminal()
        print_board(board)

#tak wyglada tablica pod"przykrywka"
#board = [
#   j      j      j
# i[0|0,  0|1,  0|2],
# i[1|0,  1|1,  1|2],
# i[2|0,  2|1,  2|2]]

        try:
            move = convert_move(choose_move())
            get_move(move, player_x, board)
        except ValueError:
            print("-------------------------------------")
            print("Podaj cyfre określająca pole od 1 do 9. ")
            print("-------------------------------------")
            continue
        game_over = is_win(board) or is_draw(board)
        player_x = not player_x
    play_again()


def convert_move(move):
    move -= 1
    return move // 3, move % 3


def is_draw(board):
    for row in board:
        for val in row:
            if val == "_":
                return False
    print_board(board)
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
            print("-----------")
            print(f"Gratulacje {winner} jesteś zwycięzcą!!")
            print("-----------")
            return True
        return False


def get_move(move, player_x, board):
    #sprawdzam czy tablica jest pusta
    #move jest tuple
    i, j = move
    if board[i][j] == "_":
        board[i][j] = "X" if player_x else "O"
    else:
        # raise ValueError
        print("To miejsce jest już zajęte., wybierz ponownie")


def print_board(board):
    cell_0 = 0
    cell_1 = 1
    cell_2 = 2
    line = "---+---+---"
    counter = 0
    numbers = 1
    for row in board:
        if counter == 0:
            template = f'    \033[36m{counter + 1}\033[0m |\033[36m{counter + 2}\033[0m | \033[36m{counter + 3}\033[0m'
        elif counter == 1:
            template = f'   \033[36m{counter + 3}\033[0m | \033[36m{counter + 4}\033[0m | \033[36m{counter + 5}\033[0m'
        else:
            template = f'   \033[36m {counter + 5} | \033[36m{counter + 6}\033[0m | \033[36m{counter + 7}\033[0m'
        print(f' {row[cell_0]} | {row[cell_1]} | {row[cell_2]} {template}')
        if counter < 2:
            print(f'{line}   {line}')
        counter += 1
        numbers += 1


#wybieram pole od 1 do 9 (input always returns a string!)


def choose_move():
    print("++++++++++++")
    move = int(input("Wybierz pole: "))
    print("++++++++++++")
    while move < 1 or move > 9:
        print("Wybierz poprawne pole, tak jak sugeruje rysunek")
        move = int(input("Wybierz pole: "))
    return move


def print_instructions():
    print("Witamy w naszej grze: Kółko i krzyżyk.\n Zasady gry sa bardzo proste, wybierasz ruch od 1 do 9.\n Wygrywa madrzejszy ;) ")


def user_name():
    name = input('Jak masz na imię?...')
    hi = input("Czy chcesz zagrać Kółko i krzyżyk? t/n")
    if hi == "tak" or hi == "t":
        print("Cześć " + name, "Pozwole Ci zacząć ..")
    else:
        sys.exit()


def play_again():
    question = input("Chcesz zagrać ponownie? t/n")
    if question == "t" or question == "tak":
        return main()
    else:
        print("Miłego dnia !!")
        sys.exit()


if __name__ == "__main__":
    main()
