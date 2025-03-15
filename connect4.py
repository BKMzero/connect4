# TODO (optional features):
# Prompt the user to play in singleplayer or multiplayer
    # In singleplayer, the user plays against a bot who randomly places pieces on the board
    # In multiplayer, the user plays against another user locally

from random import randint

board = [['O', 'O', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', 'O', 'O']]

player_names = []

def assign_players():
    # Randomly assign player 1 to either Red or Yellow, then assign player 2 to the unassigned team
    teams = ["Red", "Yellow"]
    player1 = teams[randint(0, 1)]
    teams.remove(player1)
    player2 = teams[0]
    player_names.append(player1)
    player_names.append(player2)
    return [player1[0], player2[0]]

def show_board():
    # Shows the board in a grid representation
    for row in board:
        for column in row:
            print(column, end=" ")
        print("")
    print("")

def available_columns(c):
    # Return a list of columns and remove ones which are completely filled from the list
    columns = []
    j = 1
    for i in c:
        if i != 0:
            columns.append(j)
        j += 1
    return columns

def last_in_column():
    # Return the unfilled height of every column (indices which don't contain R or Y chips)
    column = []
    for c in range(0, 7):
        row = []
        for r in board:
            row.append(r[c])
        column.append(row.count("O"))
    return column

def turn():
    # Input the user to choose a column and return the index of the respective column
    show_board()
    columns = available_columns(last_in_column())
    piece = ""
    while True:
        piece = input(f"Please enter an available column \n{columns}: ")
        if piece.isnumeric() and columns.count(int(piece)) != 0:
            break
        else:
            print("Not an available column")
    return int(piece) - 1

def win_condition(team):
    # Check if the specified team has formed 4 pieces in a row horizontally, vertically, or diagonally anywhere on the board
    length = len(board)
    for r in range(length - 1, -1, -1):
        for c in range(length, -1, -1):
            if board[r][c] == board[r][c - 1] == board[r][c - 2] == board[r][c - 3] == team and c >= 3:
                return True
            elif board[r][c] == board[r - 1][c] == board[r - 2][c] == board[r - 3][c] == team and r >= 3:
                return True
            elif board[r][c] == board[r - 1][c - 1] == board[r - 2][c - 2] == board[r - 3][c - 3] == team and c >= 3:
                return True
            elif board[r][c] == board[r - 1][c - 6] == board[r - 2][c - 5] == board[r - 3][c - 4] == team and c <= 3:
                return True
    return False

def main():
    players = assign_players()
    numOfPlayers = len(players)
    while True:
        for player in range(0, numOfPlayers):
            print(f"\n{player_names[player]}'s turn \n")
            move = turn()
            row = int(last_in_column()[move] - 1)
            board[row][move] = players[player]
            winning = win_condition(players[player])
            if winning:
                break
        if winning:
            show_board()
            print(f"{player_names[player]} wins!")
            break

if __name__ == '__main__':
    main()