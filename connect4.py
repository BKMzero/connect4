# TODO:
# Randomly assign each player to a color
# Player 1 = Red; Player 2 = Yellow
# Player 1 chooses a column to place their piece
    # Print a 2D list to represent the game board with ASCII text
    # Send the piece with the column chosen by the player to the last available row
    # If a column is full of pieces, block the player from placing pieces in that column
# Repeat for Player 2
# Repeat the previous two steps until someone connects 4 pieces either horizontally, vertically, or diagonally
    # Check for a win condition after every turn

# TODO (optional features):
# Prompt the user to play in singleplayer or multiplayer
    # In singleplayer, the user plays against a bot who randomly places pieces on the board
    # In multiplayer, the user plays against another user locally

import random

board = [['O', 'O', 'O', 'Y', 'O', 'O', 'R'],
         ['O', 'O', 'O', 'R', 'O', 'O', 'R'],
         ['O', 'Y', 'O', 'R', 'R', 'O', 'Y'],
         ['O', 'Y', 'R', 'Y', 'Y', 'R', 'R'],
         ['Y', 'Y', 'Y', 'R', 'Y', 'Y', 'Y'],
         ['R', 'R', 'Y', 'R', 'Y', 'Y', 'R']]

def assign_players():
    teams = ["Red", "Yellow"]
    player1 = teams[random.randint(0, 1)]
    teams.remove(player1)
    player2 = teams[0]
    return {"Player1": player1, "Player2": player2}

def show_board():
    for row in board:
        for column in row:
            print(column, end=" ")
        print("")
    print("")

def available_columns(c):
    # Return a list of columns and remove ones which are completely filled from the list
    columns = []
    j = 0
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
    show_board()
    piece = ""
    columns = available_columns(last_in_column())
    while columns.count(piece) == 0:
        piece = input(f"Pick a column number to place your piece: \n{columns}\n")

def main():
    players = assign_players()
    # print(players)
    turn()
    # while win_condition() != False:
    #     player_player
    pass

main()