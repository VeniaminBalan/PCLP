import numpy as np
from os import system, name

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def check_score(board: np.ndarray):
    flatten_board = board.flatten()
    score = int(sum(flatten_board))
    if any(i == 0 for i in flatten_board):
        return (score, False) # exists empty tile
    return (score, True) # no empty tile - game over

def print_board(board: np.ndarray):
    for i in range(4):
        for j in range(4):
            print(board[i][j], end=" ")
        print()

def generate_new_tile(board: np.ndarray):
    empty_tiles = np.where(board == 0)

    if len(empty_tiles) == 0:
        return board
    random_tile = np.random.choice(len(empty_tiles[0]))
    board[empty_tiles[0][random_tile], empty_tiles[1][random_tile]] = 2
    return board


def move_up(board: np.ndarray):
    for i in range(4):
        column = board[:, i]
        column = [i for i in column if i != 0]
        column += [0] * (4 - len(column))
        for j in range(len(column)-1):
            if column[j] == column[j+1]:
                column[j] = column[j] * 2
                column[j+1] = 0           
        board[:, i] = column


def move_left(board: np.ndarray):
    for i in range(4):
        row = board[i]
        row = [i for i in row if i != 0]
        row += [0] * (4 - len(row))
        for j in range(len(row)-1):
            if row[j] == row[j+1]:
                row[j] = row[j] * 2
                row[j+1] = 0           
        board[i] = row


def move_right(board: np.ndarray):
    for i in range(4):
        row = board[i]
        row = [i for i in row if i != 0]
        row += [0] * (4 - len(row))
        for j in range(len(row)-1):
            if row[j] == row[j+1]:
                row[j] = row[j] * 2
                row[j+1] = 0           
        board[i] = row[::-1]

def move_down(board: np.ndarray):
    for i in range(4):
        column = board[:, i]
        column = [i for i in column if i != 0]
        column += [0] * (4 - len(column))
        for j in range(len(column)-1):
            if column[j] == column[j+1]:
                column[j] = column[j] * 2
                column[j+1] = 0           
        board[:, i] = column[::-1]

def move_board(board: np.ndarray, move: str):
    move_fn[move](board)
    
def handle_move():
    print("Enter move: ")
    while True:
        move = input()
        match move.upper():
            case move if  move in ["W", "A", "S", "D" ]:
                return move
            case _:
                print("Invalid move")


move_fn = {
    "W": move_up,
    "A": move_left,
    "S": move_down,
    "D": move_right
}

def main():
    game_board = np.array([
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ])
    print("2048 game")
    while True:
        clear()
        game_board = generate_new_tile(game_board)
        score, game_over = check_score(game_board)
        print_board(game_board)

        if game_over:
            print("Game Over")
            print("Score: ", score)
            break

        #move the board
        move = handle_move()
        move_board(game_board, move)


if __name__ == "__main__":
    main()
