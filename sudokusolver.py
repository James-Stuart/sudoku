# Script solves sudoku puzzles. Longest time so far is ~30min.
from sudoku_aux import *
import timeit


# Entering the sudokuboard directly into the script is cumbersome. The following
# script will try to make the user interface more user-friendly.

# =============================================================================
# sudokuboard = []
# print '\nSudoku Solver: \n'
# print 'Please enter each row from top-to-bottom. Indicating empty entries'
# print 'using the number 0. Otherwise, entering the number in the square.'
# 
# =============================================================================

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
sudokuboardEasy = [row1,
               row2,
               row3,
               row4,
               row5,
               row6,
               row7,
               row8,
               row9
               ]




row1 = ['.', '.', '.',    '.', '.', '8',    '.', '3', '.']
row2 = ['.', '.', '.',    '.', '.', '.',    '4', '.', '5']
row3 = ['.', '.', '1',    '.', '.', '.',    '.', '7', '.']

row4 = ['7', '3', '.',    '.', '.', '.',    '2', '8', '.']
row5 = ['9', '5', '.',    '3', '.', '.',    '.', '.', '.']
row6 = ['.', '.', '.',    '.', '.', '6',    '.', '.', '4']

row7 = ['8', '.', '.',    '1', '4', '.',    '.', '.', '.']
row8 = ['.', '.', '.',    '8', '7', '.',    '.', '1', '6']
row9 = ['.', '.', '5',    '.', '.', '.',    '9', '.', '.']
sudokuboardMedium = [row1,
               row2,
               row3,
               row4,
               row5,
               row6,
               row7,
               row8,
               row9
               ]


row1 = ['8', '.', '.',    '.', '.', '.',    '.', '.', '.']
row2 = ['.', '.', '3',    '6', '.', '.',    '.', '.', '.']
row3 = ['.', '7', '.',    '.', '9', '.',    '2', '.', '.']

row4 = ['.', '5', '.',    '.', '.', '7',    '.', '.', '.']
row5 = ['.', '.', '.',    '.', '4', '5',    '7', '.', '.']
row6 = ['.', '.', '.',    '1', '.', '.',    '.', '3', '.']

row7 = ['.', '.', '1',    '.', '.', '.',    '.', '6', '8']
row8 = ['.', '.', '8',    '5', '.', '.',    '.', '1', '.']
row9 = ['.', '9', '.',    '.', '.', '.',    '4', '.', '.']
sudokuboardHard = [row1,
               row2,
               row3,
               row4,
               row5,
               row6,
               row7,
               row8,
               row9
               ]


# =============================================================================
# # Boolean used to make sure the correct puzzle is being solved.
# # This will help deal with nonsense input from the user.
# correct_sudoku_puzzle = False
# 
# while correct_sudoku_puzzle == False:
# 
#     # Take the input from the user.
#     for i in range(1,10):
#         print "Row %s" % i
#         row = raw_input("")
#         # Now the code wraps the input into the design choice made at the start of
#         # writing this project.
#         row = list(row)
#         row_board = []
#         for x in row:
#             if x == '0':
#                 row_board.append('.')
#             else:
#                 row_board.append(x)
#         sudokuboard.append(row_board)
# 
#     # Print the board
#     print "\nIs this the board that you would like me to solve?"
#     print print_sudoku(sudokuboard)
# 
#     correct_board = raw_input("Is the board correct?(Y/n): ")
#     if correct_board == 'Y':
#         correct_sudoku_puzzle = True
#     elif correct_board == 'n':
#         print 'Please enter the board again. Remembering to enter empty squares'
#         print 'as the number 0.'
#     else:
#         print 'Sorry, I did not understand that. '
#         print 'Please enter the board again. Remembering to enter empty squares'
#         print 'as the number 0.'
# 
# =============================================================================
#sudokuboard = sudokuboardEasy
#sudokuboard = sudokuboardMedium
sudokuboard = sudokuboardHard
# Before we get started, we should check whether the given board is valid.
if not sudokucheck(sudokuboard):
    print("The board is not valid")

# Work work work work work ...
print('\nThinking ... \n')
start = timeit.default_timer()
updated_board = sudoku_tree_solver(sudokuboard)
stop = timeit.default_timer()


if sudoku_complete(updated_board):
    print('Here is the solution to your sudoku.')
    print_sudoku(updated_board)
    print('It took %s seconds to solve this Sudoku' % (stop - start))
else:
    print('Hmmm. I seem to be stuck. I need a smarter person to code me better.')
