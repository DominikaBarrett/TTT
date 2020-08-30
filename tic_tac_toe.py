def print_board(board):
    for row in board:
        print(row)

#wybieram pole od 1 do 9 (input always returns a string!)
def get_move():
    move = int(input("Wybierz pole: "))
    if not 1 <= move <= 9:
        raise ValueError
    return move


#definiuje tablice jako liste list i wykluczam error
board = [["_" for _ in range(3)] for _ in range(3)]
try:
    move = get_move()
    print(move)
except ValueError:
    print("Prosze wybrac z przedzialu od 1-9")