# This script (normally) solves Su Doku puzzles "ranked easy"
from sudoku_aux import *


# These are some sudoku boards to test the code on.
# This naive method simply fills in the entries with one option. Checks the
# new board for entries with one option and fills those in. Repeating until
# board has no entries with one option. This does not necessarily solve the
# puzzle; it maybe that this method returns an incomplete board. Indeed, for
# puzzles ranked medium (or harder) more is required to solve the board.


# Both of these boards are considered "easy" by the source website.

# row1 = ['5', '3', '.',    '.', '7', '.',    '.', '.', '.']
# row2 = ['6', '.', '.',    '1', '9', '5',    '.', '.', '.']
# row3 = ['.', '9', '8',    '.', '.', '.',    '.', '6', '.']
#
# row4 = ['8', '.', '.',    '.', '6', '.',    '.', '.', '3']
# row5 = ['4', '.', '.',    '8', '.', '3',    '.', '.', '1']
# row6 = ['7', '.', '.',    '.', '2', '.',    '.', '.', '6']
#
# row7 = ['.', '6', '.',    '.', '.', '.',    '2', '8', '.']
# row8 = ['.', '.', '.',    '4', '1', '9',    '.', '.', '5']
# row9 = ['.', '.', '.',    '.', '8', '.',    '.', '7', '9']

row1 = ['3', '2', '8',    '.', '7', '.',    '.', '1', '5']
row2 = ['.', '7', '6',    '.', '.', '.',    '8', '9', '3']
row3 = ['4', '.', '.',    '1', '.', '.',    '.', '6', '.']

row4 = ['5', '.', '.',    '3', '.', '.',    '.', '7', '.']
row5 = ['.', '.', '.',    '8', '1', '.',    '6', '3', '.']
row6 = ['6', '.', '.',    '.', '4', '.',    '9', '.', '.']

row7 = ['.', '6', '2',    '5', '9', '7',    '.', '.', '.']
row8 = ['9', '.', '.',    '.', '3', '.',    '7', '.', '.']
row9 = ['7', '4', '3',    '.', '2', '1',    '.', '8', '.']


# Defines the board the script will solve.
sudokuboard = [row1,
               row2,
               row3,
               row4,
               row5,
               row6,
               row7,
               row8,
               row9
               ]


# The heart of the script starts from here.

# Print the board
print(print_sudoku(sudokuboard))
print("This is the board to be solved.")

# Before we get started, we should check whether the given board is valid.
if sudokucheck(sudokuboard) == False:
    print("The board is not valid")
    exit()
else:
    pass

# This does the work.
sudoku_oneoption(sudokuboard)

# Print the work done so far.
if sudoku_complete(sudokuboard):
    print_sudoku(sudokuboard)
    print('This board has been solved. \n\n')
else:
    print_sudoku(sudokuboard)
    print('More work needs to be done to complete this board.\n\n')
